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

public interface Position2D
{
    public int getX();
    public int getY();
    public boolean setX(int newX);  /* return true if x is changed */
    public boolean setY(int newY);  /* return true if y is changed */
    public void moveTo(int newX, int newY);
    public void setObject(Object obj);

    public static final int DEFAULT_DISTANCE = 1;

    default public void move(Direction direction, int distance)
    {
        if (distance == 0)
            return;
        switch direction
        {
            case N:
                System.out.println("case N");
                moveTo(
                        getX(),
                        getY() + distance
                      );
                break;
            case E:
                moveTo(
                        getX() + distance,
                        getY()
                      );
                break;
            case S:
                move(Direction.N, - distance);
                break;
            case W:
                move(Direction.E, - distance);
                break;
            case NE:
                move(Direction.N, distance);
                move(Direction.E, distance);
                break;
            case SE:
                move(Direction.S, distance);
                move(Direction.E, distance);
                break;
            case SW:
                move(Direction.S, distance);
                move(Direction.W, distance);
                break;
            case NW:
                move(Direction.N, distance);
                move(Direction.W, distance);
                break;
            default:
                System.err.println("Position2D: direction not understood");
                break;
        }
    }

    default public void move(Direction direction)
    {
        move(direction, DEFAULT_DISTANCE);
    }

    /* return true if x or y is changed */
    default public void setCoordinates(int x, int y)
    { 
        return setX(x) | setY(y);
    }

    /* alter value so that min <= value < max */
    public static int fitIntoRange(int value, int min, int max)
    // min < max
    {
        while (value < min)
            value += max;    // value < max
        while (value >= max)
            value -= max;    // value >= 0
        return value;
    }
}

public class Position implements Position2D
{
// instance variables

    private Object[][] map;
    private int x, y;

// static fields

/* public */

// constructors

    Position2D(Object[][] map, int x, int y)
    {
        this.map = map;
        setCoordinates(x, y);
    }

// instance methods

    @Override public void moveTo(int newX, int newY)
    {
        int oldX = x, oldY = y;
        if (setCoordinates(newX, newY))
        {
            Object bak = map[x][y];
            map[x][y] = map[oldX][oldY];
            map[oldX][oldY] = bak;
        }
    }

    public void moveLeft(int distance)
    {
        moveTo(
                getX() - distance,
                getY()
              );
    }

    public void moveRight(int distance)
    {
        moveTo(
                getX() + distance,
                getY()
              );
    }

    public void moveDown(int distance)
    {
        moveTo(            
                getX(),
                getY() - distance
              );
    }

    public void moveUp(int distance)
    {
        moveTo(
                getX(),
                getY() + distance
              );
    }

    public void moveLeft()  { moveLeft  ( DEFAULT_DISTANCE ); }
    public void moveRight() { moveRight ( DEFAULT_DISTANCE ); }
    public void moveDown()  { moveDown  ( DEFAULT_DISTANCE ); }
    public void moveUp()    { moveUp    ( DEFAULT_DISTANCE ); }

 // getters

    @Override public int getX() { return x; }
    @Override public int getY() { return y; }

 // setters

    @Override public void setObject(Object obj)
    {
        map[x][y] = obj;
    }

    @Override public boolean setX(int newX)
    {
        int oldX = x;
        x = fitIntoRange(newX, 0, map.getWidth());
        return oldX != x;
    }

    @Override public boolean setY(int newY)
    {
        int oldY = y;
        y = fitIntoRange(newY, 0, map.getHeight());
        return oldY != y;
    }

// static methods

/* private */

// constructors

// instance methods

 // getters

 // setters

// static methods

}
