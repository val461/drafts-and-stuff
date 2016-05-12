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

package cards;

public class Deck
{
	private Card[] cards;
	private static int size;

	public Deck()
	{
		this(52);
	}

	public Deck(int maxsize)
	{
		assert maxsize > 0;
		cards = new Card[maxsize];
		size = 0;
	}

	public void showCards()
	{
		for (int i = 0; i < size; i++)
			System.out.println(this.getCard(i).toString());
	}

	public Card getCard(int i)
	{
		assert i >= 0;
		assert i < size;
		return cards[i];
	}

	public boolean addCard(Card newCard)
	{
		if (size < cards.length)
		{
			cards[size++] = newCard;
			return true;
		}
		else
		{
			return false;
		}
	}

	public boolean removeLastCard()
	{
		if (size > 0)
		{
			cards[--size] = null;
			return true;
		}
		else
		{
			return false;
		}
	}

	public void setCardAt(int i, Card newCard)
	{
		assert i > 0;
		assert i < cards.length;
		cards[i] = newCard;
	}
}

