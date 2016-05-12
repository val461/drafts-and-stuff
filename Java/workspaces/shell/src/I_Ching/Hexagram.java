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

public class Hexagram implements Xgram
{
// static fields

    public static final int LENGTH = 2;

// instance variables

    private Trigram[] trigrams = new Trigram[LENGTH];
    private int id = -1;
    private String name = null;
    private String asciiart = null;
    private String description = null;

/* public */

// constructors

    Hexagram()
    {
        for (int i = 0; i < LENGTH; i++)
            trigrams[i] = new Trigram();
    }

    Hexagram(Trigram... trigrams)
    {
        this.trigrams = trigrams;
    }

    Hexagram(Line... lines)
    {
        for (int i = 0, j = 0; i < LENGTH; i++, j += 3)
            this.trigrams[i] = new Trigram(lines[j], lines[j+1], lines[j+2]);
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
            for (Trigram trigram : trigrams)
                string.insert(0, trigram.getAsciiArt());
            asciiart = string.toString();
        }
        return asciiart;
    }

    @Override
    public String getName()
    {
        if (name == null)
            name = Hexagrams.withId(getId()).toString();
        return name;
    }

    @Override
    public int getId()
    {
        if (id < 0)
            id = Integer.parseInt(toBinary(), 2);
        return id;
    }
/*
    public String toBinary()
    {
        StringBuilder binary = new StringBuilder();

        for (Trigram trigram : trigrams)
            binary.append(trigram.toBinary()); // append() instead of insert() because arabic numerals are written from right to left

        return binary.toString();
    }
*/
    @Override
    public Xgram next()
    {
        Trigram[] next = new Trigram[LENGTH];

        for (int i = 0; i < LENGTH; i++)
            next[i] = (Trigram) trigrams[i].next();

        return new Hexagram(next);
    }

    @Override
    public Xgram[] getSubgrams()
    {
        return this.trigrams;
    }

// static methods

    public static Hexagram fromBinary(String code)
    {
        Trigram[] trigrams = new Trigram[LENGTH];

        for (int i = 0, j = 0; i < LENGTH; i++, j += Trigram.LENGTH)
            trigrams[i] = Trigram.fromBinary(code.substring(j, j+2));   // FIXME check usage for String.substring() or similar in Javadoc

        return new Hexagram(trigrams);
    }

    public static Hexagram withId(String id)
    {
        return withId(Integer.parseInt(id));
    }

    public static Hexagram withId(int id)
    {
        return fromBinary(Integer.toString(id, 2));
    }

    public static void main(String[] args)
    {
        Hexagram h, n;
        if (args.length > 0)
            if (args[0].length() > 2)
                h = Hexagram.fromBinary(args[0]);
            else
                h = Hexagram.withId(args[0]);
        else
            h = new Hexagram();
        System.out.println(h.toBinary());
        System.out.println(h.toString());
        n = (Hexagram) h.next();
        System.out.println(n.toBinary());
        System.out.println(n.toString());
    }

/* private */

// instance methods

 // getters

 // setters

// static methods

}
