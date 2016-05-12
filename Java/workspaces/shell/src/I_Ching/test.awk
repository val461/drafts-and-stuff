#!/bin/awk -f

BEGIN {
    line = 0;
    count = 0;
# parameters:
    first_line = 39;
    last_line = 103;
    word = "SKY";
}

{
    if (line < last_line) {
        line++;
        if(line >= first_line) {
            if (count % 9 == 0) {
                str = "    " $1 word;
                $0 = str substr($0, length(str) + 1);
#                sub("_", "_" word, $1);
            }
            count++;
        }
    }
    print;
}
