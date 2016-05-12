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
	final public int DECK_SIZE = 52;

	public static void main(String[] args)
	{
		Deck deck = new Deck();
		deck.showCards();
	}
	
	public Deck()
	{
		int i = 0;
		cards = new Card[DECK_SIZE];
		for (Rank rank : Rank.values())
			for (Suit suit : Suit.values())
				cards[i++] = new Card(rank, suit);
	}

	@Override
	public boolean equals(Object otherDeck)
	{
		return otherDeck.hashCode() == hashCode();
	}

	@Override
	public int hashCode()
	{
		return java.util.Arrays.hashCode(cards);
	}

	public void showCards()
	{
		System.out.print(this);
	}

	public String toString()
	{
		String result = new String();
		for (Card card : cards)
			result += card + "\n";
		return result;
	}

	public Card getCard(int i)
	{
		if (0 <= i && i < DECK_SIZE)
			return cards[i];
		else
		{
			System.err.println("Error: no card at index " + i);
			return null;
		}
	}
}

