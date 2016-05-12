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

public enum Hexagrams
{
    EARTH_EARTH             ( 0,  2, "", ""),
    EARTH_MOUNTAIN          ( 1, 23, "", ""),
    EARTH_CANYON            ( 2,  8, "", ""),
    EARTH_WIND              ( 3, 20, "", ""),
    EARTH_THUNDER           ( 4, 16, "", ""),
    EARTH_FIRE              ( 5, 35, "", ""),
    EARTH_LAKE              ( 6, 45, "", ""),
    EARTH_SKY               ( 7, 12, "", ""),

    MOUNTAIN_EARTH          ( 8, 15, "", ""),
    MOUNTAIN_MOUNTAIN       ( 9, 52, "", ""),
    MOUNTAIN_CANYON         (10, 39, "", ""),
    MOUNTAIN_WIND           (11, 53, "", ""),
    MOUNTAIN_THUNDER        (12, 62, "", ""),
    MOUNTAIN_FIRE           (13, 56, "", ""),
    MOUNTAIN_LAKE           (14, 31, "", ""),
    MOUNTAIN_SKY            (15, 33, "", ""),

    CANYON_EARTH            (16,  7, "", ""),
    CANYON_MOUNTAIN         (17,  4, "", ""),
    CANYON_CANYON           (18, 29, "", ""),
    CANYON_WIND             (19, 59, "", ""),
    CANYON_THUNDER          (20, 40, "", ""),
    CANYON_FIRE             (21, 64, "", ""),
    CANYON_LAKE             (22, 47, "", ""),
    CANYON_SKY              (23,  6, "", ""),

    WIND_EARTH              (24, 46, "", ""),
    WIND_MOUNTAIN           (25, 18, "", ""),
    WIND_CANYON             (26, 48, "", ""),
    WIND_WIND               (27, 57, "", ""),
    WIND_THUNDER            (28, 32, "", ""),
    WIND_FIRE               (29, 50, "", ""),
    WIND_LAKE               (30, 28, "", ""),
    WIND_SKY                (31, 44, "", ""),

    THUNDER_EARTH           (32, 24, "", ""),
    THUNDER_MOUNTAIN        (33, 27, "", ""),
    THUNDER_CANYON          (34,  3, "", ""),
    THUNDER_WIND            (35, 42, "", ""),
    THUNDER_THUNDER         (36, 51, "", ""),
    THUNDER_FIRE            (37, 21, "", ""),
    THUNDER_LAKE            (38, 17, "", ""),
    THUNDER_SKY             (39, 25, "", ""),

    FIRE_EARTH              (40, 36, "", ""),
    FIRE_MOUNTAIN           (41, 22, "", ""),
    FIRE_CANYON             (42, 63, "", ""),
    FIRE_WIND               (43, 37, "", ""),
    FIRE_THUNDER            (44, 55, "", ""),
    FIRE_FIRE               (45, 30, "", ""),
    FIRE_LAKE               (46, 49, "", ""),
    FIRE_SKY                (47, 13, "", ""),

    LAKE_EARTH              (48, 19, "", ""),
    LAKE_MOUNTAIN           (49, 41, "", ""),
    LAKE_CANYON             (50, 60, "", ""),
    LAKE_WIND               (51, 61, "", ""),
    LAKE_THUNDER            (52, 54, "", ""),
    LAKE_FIRE               (53, 38, "", ""),
    LAKE_LAKE               (54, 58, "", ""),
    LAKE_SKY                (55, 10, "", ""),

    SKY_EARTH               (56, 11, "", ""),
    SKY_MOUNTAIN            (57, 26, "", ""),
    SKY_CANYON              (58,  5, "", ""),
    SKY_WIND                (59,  9, "", ""),
    SKY_THUNDER             (60, 34, "", ""),
    SKY_FIRE                (61, 14, "", ""),
    SKY_LAKE                (62, 43, "", ""),
    SKY_SKY                 (63,  1, "", "");

    private static final int length = values().length;

    private final int id;
    private final int KingWenId;
    private final String name;
    private final String description;


    Hexagrams(int id, int KingWenId, String name, String description)
    {
        this.id = id;
        this.KingWenId = KingWenId;
        this.name = name;
        this.description = description;
    }

    public static Hexagrams withId(int id)
    {
        return (0 <= id && id < length) ? values()[id] : null;
    }

    public static void main(String[] args)
    {
        System.out.println(Hexagrams.withId(2));
    }

    public int     id()          { return id;                   }
//  public String  toString()    { return name;                 }
}
