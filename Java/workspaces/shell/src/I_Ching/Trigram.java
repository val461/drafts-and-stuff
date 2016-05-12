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

package I_Ching;

public class Trigram implements Xgram
{
// static fields

    public static final int LENGTH = 3;
    private static Random gen = new Random(Line.values(), Line.probabilities());

// instance variables

    private Line[] lines = new Line[LENGTH];

    private int id = -1;
    private String name = null;
    private String asciiart = null;
    private String description = null;


/* public */

// constructors

    Trigram()
    {
        getRandomLines();
    }

    Trigram(Line... lines)
    {
        this.lines = lines;
    }

// instance methods

 // getters

    @Override
    public String toString()
    {
        if (description == null)
        {
            description = getId()   + "\n"
                        + getName() + "\n"
                        + getAsciiArt();
        }
        return description;
    }

    @Override
    public String getAsciiArt()
    {
        if (asciiart == null)
        {
            StringBuilder string = new StringBuilder();

            for (Line line : lines)
                string.insert(0, line.toString() + "\n");  // insert() because hexagrams (and thus trigrams) are written upwards

            asciiart = string.toString();
        }
        return asciiart;
    }

    @Override
    public String getName()
    {
        if (name == null)
            name = Trigrams.withId(getId()).toString();
        return name;
    }

    @Override
    public int getId()
    {
        if (id < 0)
            id = Integer.parseInt(toBinary(), 2);
        return id;
    }

    @Override
    public String toBinary()
    {
        StringBuilder binary = new StringBuilder();

        for (Line line : lines)
            binary.append(line.toBinary()); // bottom line is most significant bit

        return binary.toString();
    }

    @Override
    public Xgram next()
    {
        Line[] next = new Line[LENGTH];

        for (int i = 0; i < LENGTH; i++)
            next[i] = (Line) lines[i].next();

        return new Trigram(next);
    }

    @Override
    public Xgram[] getSubgrams()
    {
        return lines;
    }

// static methods

    public static Trigram fromBinary(String code)
    {
        Line[] lines = new Line[LENGTH];

        for (int i = 0; i < LENGTH; i++)
            lines[i] = Line.fromBinary(code.charAt(i));

        return new Trigram(lines);
    }

    public static Trigram withId(String id)
    {
        return withId(Integer.parseInt(id));
    }

    public static Trigram withId(int id)
    {
        return fromBinary(Integer.toString(id, 2));
    }

    public static void main(String[] args)
    {
        Trigram t, n;
        if (args.length > 0)
            if (args[0].length() > 2)
                t = Trigram.fromBinary(args[0]);
            else
                t = Trigram.withId(args[0]);
        else
            t = new Trigram();
        System.out.println(t.toBinary());
        System.out.println(t.toString());
        n = (Trigram) t.next();
        System.out.println(n.toBinary());
        System.out.println(n.toString());
    }

/* private */

// instance methods

    private void getRandomLines()
    {
        for (int i = 0; i < LENGTH; i++)
            lines[i] = getRandomLine();
    }

    private Line getRandomLine()
    {
        return (Line) gen.pick();
    }

 // getters

 // setters

// static methods

}
