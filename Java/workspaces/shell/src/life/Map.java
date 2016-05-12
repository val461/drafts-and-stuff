/*
	This is free and unencumbered software released into the public domain.

	Anyone is free to copy, modify, publish, use, compile, sell, or
	distribute this software, either in source code form or as a compiled
	binary, for any purpose, commercial or non-commercial, and by any
	means.

	In jurisdictions that recognize copyright laws, the author or authors
	of this software dedicate any and all copyright interest in the
	software to the public domain. We make this dedication for the benefit
	of the public at large and to the detriment of our heirs and
	successors. We intend this dedication to be an overt act of
	relinquishment in perpetuity of all present and future rights to this
	software under copyright law.

	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
	EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
	MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
	IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
	OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
	ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
	OTHER DEALINGS IN THE SOFTWARE.

	For more information, please refer to <http://unlicense.org/>
*/

package life;
import static Consts.*;

public class Map
{
// instance variables

    private Object[][] map;
    private int width;
    private int height;

// static fields

/* public */

// constructors

    Map(int width, int height)
    // width and height > 0
    {
        this.map = new Object[width][height];
        actualizeDimensions();
    }

// instance methods

    public void display()
    {
        //TODO
    }

    public Position2D add(Object obj, int x, int y)
    // 0 <= x < width
    // 0 <= y < height
    {
        map[x][y] = obj;
        return new Position2D(this, x, y);
    }

 // getters

    public int getWidth()   { return width; }
    public int getHeight()  { return height; }

 // setters

// static methods

    public static void main(String[] args)
    {
        Map m = new Map(4, 4);
        Position2D p = new Position(this, 0, 0);
        Animal a = new Animal(p);
    }

/* private */

// constructors

// instance methods

 // getters

 // setters

    private final void actualizeDimensions()
    {
        width  = map.length;
        height = map[0].length;
    }

// static methods

}
