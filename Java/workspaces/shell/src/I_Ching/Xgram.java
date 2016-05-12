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

public interface Xgram
{
    default public String getAsciiArt()
    {
        StringBuilder string = new StringBuilder();

        for (Xgram subgram : getSubgrams())
            string.insert(0, subgram.getAsciiArt());

        return string.toString();
    }

    default public int getId()
    {
        return Integer.parseInt(toBinary(), 2);
    }

    default public String toBinary()
    {
        StringBuilder binary = new StringBuilder();

        for (Xgram subgram : getSubgrams())
            binary.append(subgram.toBinary()); // append() instead of insert() because arabic numerals are written from right to left

        return binary.toString();
    }

    public String getName();
    public Xgram   next();
    public Xgram[] getSubgrams();
}
