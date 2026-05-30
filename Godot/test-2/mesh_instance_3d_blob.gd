extends MeshInstance3D

var rings = 50
var radial_segments = 50
var radius = 1

var fnl = FastNoiseLite.new()
var mdt = MeshDataTool.new()

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	# 1. Create sphere
	
	var surface_array = []
	surface_array.resize(Mesh.ARRAY_MAX)
	var verts = PackedVector3Array()
	var uvs = PackedVector2Array()
	var normals = PackedVector3Array()
	var indices = PackedInt32Array()

	# https://aistudio.google.com/prompts/12BLlKms-SE1THYh7pGQuOjzV26WFoY6a

	# Vertex indices.
	var thisrow = 0
	var prevrow = 0
	var point = 0

	# Loop over rings.
	for i in range(rings + 1):
		var v = float(i) / rings
		var w = sin(PI * v)
		var y = cos(PI * v)

		# Loop over segments in ring.
		for j in range(radial_segments + 1):
			var u = float(j) / radial_segments
			var x = sin(u * PI * 2.0)
			var z = cos(u * PI * 2.0)
			var vert = Vector3(x * radius * w, y * radius, z * radius * w)
			verts.append(vert)
			normals.append(vert.normalized())
			uvs.append(Vector2(u, v))
			point += 1

			# Create triangles in ring using indices.
			if i > 0 and j > 0:
				indices.append(prevrow + j - 1)
				indices.append(prevrow + j)
				indices.append(thisrow + j - 1)

				indices.append(prevrow + j)
				indices.append(thisrow + j)
				indices.append(thisrow + j - 1)

		prevrow = thisrow
		thisrow = point

	surface_array[Mesh.ARRAY_VERTEX] = verts
	surface_array[Mesh.ARRAY_TEX_UV] = uvs
	surface_array[Mesh.ARRAY_NORMAL] = normals
	surface_array[Mesh.ARRAY_INDEX] = indices

	mesh = ArrayMesh.new() 
	# No blendshapes, lods, or compression used.
	mesh.add_surface_from_arrays(Mesh.PRIMITIVE_TRIANGLES, surface_array)
	
	# 2. Turn sphere into blob

	randomize()
	fnl.set_seed(randi())
	fnl.frequency = .7

	mdt.create_from_surface(mesh, 0)

	for i in range(mdt.get_vertex_count()):
		var vertex = mdt.get_vertex(i).normalized()
		# Scale the vertices using noise.
		vertex = vertex * (fnl.get_noise_3dv(vertex) * .5 + .75)
		mdt.set_vertex(i, vertex)

	# Calculate the vertex normals, face-by-face.
	for i in range(mdt.get_face_count()):
		# Get the index in the vertex array.
		var a = mdt.get_face_vertex(i, 0)
		var b = mdt.get_face_vertex(i, 1)
		var c = mdt.get_face_vertex(i, 2)
		# Get the vertex position using the vertex index.
		var ap = mdt.get_vertex(a)
		var bp = mdt.get_vertex(b)
		var cp = mdt.get_vertex(c)
		# Calculate the normal of the face.
		var n = (bp - cp).cross(ap - bp).normalized()
		# Add this face normal to the current vertex normals.
		# This will not result in perfect normals, but it will be close.
		mdt.set_vertex_normal(a, n + mdt.get_vertex_normal(a))
		mdt.set_vertex_normal(b, n + mdt.get_vertex_normal(b))
		mdt.set_vertex_normal(c, n + mdt.get_vertex_normal(c))

	# Run through the vertices one last time to normalize their normals and
	# set the vertex colors to these new normals.
	for i in range(mdt.get_vertex_count()):
		var v = mdt.get_vertex_normal(i).normalized()
		mdt.set_vertex_normal(i, v)
		mdt.set_vertex_color(i, Color(v.x, v.y, v.z))

	mesh.clear_surfaces()
	mdt.commit_to_surface(mesh)

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	pass
