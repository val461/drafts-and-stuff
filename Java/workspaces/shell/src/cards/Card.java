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
	// constants
	//	ranks
	public static final int ACE   = 1;
	public static final int DEUCE = 2;
	public static final int THREE = 3;
	public static final int FOUR  = 4;
	public static final int FIVE  = 5;
	public static final int SIX   = 6;
	public static final int SEVEN = 7;
	public static final int EIGHT = 8;
	public static final int NINE  = 9;
	public static final int TEN   = 10;
	public static final int JACK  = 11;
	public static final int QUEEN = 12;
	public static final int KING  = 13;
	//	suits
	public static final int SPADES = 14;
	public static final int DIAMONDS = 15;
	public static final int HEARTS = 16;
	public static final int CLUBS = 17;
	// instance variables
	private int rank;
	private int suit;

	public Card()
	{
		this(ACE, SPADES);
	}

	public Card(int rank, int suit)
	{
		if (!this.set(rank, suit))
			this.set(ACE, SPADES);
	}

	public String toString()
	{
		return getRank() + " of " + getSuit();
	}
	
	public String getRank() { return rankToString(rank); }
	public String getSuit() { return suitToString(suit); }

	public static String rankToString(int rank)
	{
		switch (rank)
		{
			case ACE:
				return "Ace";
			case DEUCE:
				return "Deuce";
			case THREE:
				return "Three";
			case FOUR:
				return "Four";
			case FIVE:
				return "Five";
			case SIX:
				return "Six";
			case SEVEN:
				return "Seven";
			case EIGHT:
				return "Eight";
			case NINE:
				return "Nine";
			case TEN:
				return "Ten";
			case JACK:
				return "Jack";
			case QUEEN:
				return "Queen";
			case KING:
				return "King";
			default:
				//Handle an illegal argument.  There are generally two
				//ways to handle invalid arguments, throwing an exception
				//(see the section on Handling Exceptions) or return null
				return null;
		}	
	}

	public static String suitToString(int suit)
	{
		switch (suit)
		{
			case DIAMONDS:
				return "Diamonds";
			case CLUBS:
				return "Clubs";
			case HEARTS:
				return "Hearts";
			case SPADES:
				return "Spades";
			default:
				return null;
		}	
	}

	public boolean set(int rank, int suit)
	{
		return setRank(rank) && setSuit(suit);
	}

	public boolean setRank(int rank)
	{
		if (ACE <= rank && rank <= KING)
		{
			this.rank = rank;
			return true;
		}
		else
		{
			return false;
		}
	}

	public boolean setSuit(int suit)
	{
		if (SPADES <= suit && suit <= CLUBS)
		{
			this.suit = suit;
			return true;
		}
		else
		{
			return false;
		}
	}
}

