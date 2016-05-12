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

public class Card
{
// instance variables
	private Rank rank;
	private Suit suit;
// constructors
	public Card() {this(Rank.ACE, Suit.SPADES);}
	public Card(Rank rank, Suit suit)	{this.set(rank, suit);}
// methods
	@Override
	public boolean equals(Object otherCard)
	{
		Card card = (Card) otherCard;
		return card.getRank() == getRank() && card.getSuit() == getSuit();
	}

	@Override
	public int hashCode()
	{
		return new Integer("" + getRank().toInteger() + getSuit().toInteger());
	}

	public void setRank(Rank rank)	{this.rank = rank;}
	public void setSuit(Suit suit)	{this.suit = suit;}
	public void set(Rank rank, Suit suit)
	{
		setRank(rank);
		setSuit(suit);
	}


	public Rank getRank()	{return rank;}
	public Suit getSuit()	{return suit;}
	public String toString()
	{
		return getRank() + " of " + getSuit();
	}
}

