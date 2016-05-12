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

public enum Line implements Xgram
{
    OLD_YIN     (6, 1.0/16, "─ X ─", " yin", true,  Taiji.YIN),
    YOUNG_YANG  (7, 5.0/16, "─────", "yang", false, Taiji.YANG),
    YOUNG_YIN   (8, 7.0/16, "── ──", " yin", false, Taiji.YIN),
    OLD_YANG    (9, 3.0/16, "──O──", "yang", true,  Taiji.YANG);

    private enum Taiji
    {
        YIN (0),
        YANG(1);

        private final int code;

        Taiji(int code)
        {
            this.code = code;
        }

        public int toBinary()
        {
            return code;
        }

        public String toBinaryString()
        {
            return Integer.toString(code);
        }
    }

    private final int id;
    private final double probability;
    private final String asciiart;
    private final String name;
    private String description = null;
    private final boolean moving;
    private final Taiji form;

    private static double[] probabilities = null;


    Line(int id, double probability, String asciiart, String name, boolean moving, Taiji form)
    {
        this.id = id;
        this.probability = probability;
        this.name = name;
        this.asciiart = asciiart;
        this.moving = moving;
        this.form = form;
    }

    @Override
    public int getId()
    {
        return id;                       
    }

    @Override
    public String toBinary()
    {
        return form.toBinaryString();
    }

    @Override
    public String toString()
    {
        if (description == null)
            description = getAsciiArt() + "\t" + getName();
        return description;
    }

    @Override
    public String getAsciiArt()
    {
        return asciiart;
    }

    @Override
    public String getName()
    {
        return name;
    }

    @Override
    public Xgram next()
    {
        if (this.isMoving())
            if (this.isYin())
                return YOUNG_YANG;
            else if (this.isYang())
                return YOUNG_YIN;
            else
                return null;    // not reached
        else
            return this;
    }

    @Override
    public Xgram[] getSubgrams()
    {
        return null;    // no subgrams, the Line class is the base unit
    }

    public double  probability() { return probability;              }
    public boolean isMoving()    { return moving;                   }
    public boolean isYin()       { return form == Taiji.YIN;        }
    public boolean isYang()      { return form == Taiji.YANG;       }

    public static double[] probabilities()
    {
        if (probabilities == null)
        {
            probabilities = new double[values().length];
            int i = 0;
            for (Line value : values())
            {
                probabilities[i] = value.probability;
                i++;
            }
        }
        return probabilities;
    }

    public static Line fromBinary(String code)  // alias
    {
        return fromBinary(Integer.parseInt(code));
    }

    public static Line fromBinary(char code)    // alias
    {
        return fromBinary(Character.digit(code, 4));
    }

    public static Line fromBinary(int code)     // actual function
    {
        if (code == Taiji.YIN.toBinary())
            return YOUNG_YIN;

        else if (code == Taiji.YANG.toBinary())
            return YOUNG_YANG;

        else if (code == Taiji.YIN.toBinary() + 2)
            return OLD_YIN;

        else if (code == Taiji.YANG.toBinary() + 2)
            return OLD_YANG;

        else return null;
    }
}
