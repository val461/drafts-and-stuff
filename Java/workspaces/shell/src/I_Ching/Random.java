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

public class Random
{
// instance variables

    private final int NUMBER_OF_VALUES;
    private int NUMBER_OF_PROBABILITIES;
    private double[] probabilities;
    private Object[] values;

// static fields

/* public */

// constructors

    Random(Object[] values, double... probabilities)
    {
        NUMBER_OF_PROBABILITIES = Math.min(probabilities.length, values.length);
        NUMBER_OF_VALUES = values.length;
        
        this.values = values;
        this.probabilities = new double[NUMBER_OF_PROBABILITIES];

        int i = 0;
        this.probabilities[i] = probabilities[i];

        for (i = 1; i < NUMBER_OF_PROBABILITIES && this.probabilities[i-1] < 1; i++)
        {
            this.probabilities[i] = this.probabilities[i-1] + probabilities[i];
        }

        NUMBER_OF_PROBABILITIES = i;

        /*DEBUG
        i = 0;
        for (double d : this.probabilities)
        {
            System.out.print(d);
            if (i < NUMBER_OF_PROBABILITIES)
                System.out.print(" (Y)");
            else
                System.out.print(" (N)");
            System.out.println();
            i++;
        }//*/
    }

// instance methods

 // getters

    public Object pick()
    {
        int index = pickIndex();
        if (index < NUMBER_OF_VALUES)
            return values[index];
        else
            return null;
    }

    public Object pickValue()
    {
        return pick();
    }

    public int pickIndex()
    {
        int i;
        double rand = Math.random();

        for (i = 0; i < NUMBER_OF_PROBABILITIES; i++)
            if (rand < probabilities[i])
                break;

        return i;
    }
    
 // setters

// static methods

    public static void main(String[] args)
    {
        Integer[] values = {1,2};
        double[]  probabilities = {0.4, 0.2};
        Random gen = new Random(values, probabilities);
        for (int i = 0; i < 10; i++)
            System.out.println(gen.pick());
    }

/* private */

// instance methods

 // getters
    
 // setters

// static methods

}

