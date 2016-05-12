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

package utils;

public class ReverseSequence implements CharSequence
{
// Fields
	private char[] sequence;
	private char[] reverse;

// Constructors
	public ReverseSequence(char[] sequence)
	{
		setSequence(sequence);
	}

	public ReverseSequence(String str)
	{
		this(str.toCharArray());
	}

	public ReverseSequence(CharSequence sequence)
	{
		this(sequence.toString());
	}

	public ReverseSequence()
	{
		setSequence(new char[0]);
	}

	public ReverseSequence(char[] sequence, boolean reverse)
	{
		if (reverse)
			setSequence(sequence);
		else
		{
			this.sequence = reverse(sequence);
			this.reverse = sequence;
		}
	}

// Methods
	public char charAt(int index)
	{
		return reverse[index];
	}

	public int length()
	{
		return reverse.length;
	}

	public CharSequence subSequence(int start, int end)
	{
		if (start < 0)
			start = 0;
		if (end > reverse.length)
			end = reverse.length;

		char[] subSequence = new char[end > start ? end - start : 0];

		for	(
				int i = start, j = 0;
				i < end;
				i++, j++
			)
			{ // 0 <= start <= i < end <= reverse.length
				subSequence[j] = reverse[i];
			}

		return new ReverseSequence(subSequence, false);
	}

	public String toString()
	{
		return new String(this.toCharArray());
	}

	public char[] toCharArray()
	{
		return reverse;
	}

	public static String reverse(String str)
	{
		return new String(reverse(str.toCharArray()));
	}

	public static char[] reverse(char[] sequence)
	{
		int i = sequence.length;
		char[] reverse = new char[i];

		for (char c : sequence)
			reverse[--i] = c;

		return reverse;
	}

	private void setSequence(char[] sequence)
	{
		this.sequence = sequence;
		setReverse();
	}

	private void setReverse()
	{
		reverse = reverse(sequence);
	}

	public static void main(String[] args)
	{
		CharSequence s = new ReverseSequence("Select one of the sentences from this book to use as the data.");
		System.out.println(s);
		System.out.println(s.subSequence(4, 18));
	}
}

