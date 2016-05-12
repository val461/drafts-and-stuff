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

package proofchecker;

public interface ProofChecker
{
    public void update();
}

class SystemOfPropositions implements ProofChecker
{
// instance variables

    Proposition[] propositions;

// static fields

/* public */

// constructors

// instance methods

    /*
        TODO’s:
            parse propositions from an indented file
            print propositions tree-like
    */

    @Override public void update()
    {
        startSearch:
        while (true)
        {
            for (Proposition prop : this.propositions)
                if (prop != null && prop.value() == LogicalState.UNCERTAIN)
                    if (prop.setValue())
                        continue startSearch;
            break;
        }
    }

    public void print()
    {
        for (Proposition prop : this.propositions)
        {
            if (prop != null)
                System.out.println(prop.value() + prop.desc());
        }
    }

 // getters

 // setters

// static methods

    public static void main(String[] args)
    {
        SystemOfPropositions syst = new SystemOfPropositions();
        syst.propositions = new Prop[10];
        /*
            F	2+2=4
            D		2+2=3+1
            C			2+1=3
            B			2+2=2+1+1
            A				2=1+1
            E		3+1=4
        */
        Proposition A = new Prop("2=1+1"),
                    B = new Prop("2+2=2+1+1"),
                    C = new Prop("2+1=3"),
                    D = new Prop("2+2=3+1"),
                    E = new Prop("3+1=4"),
                    F = new Prop("2+2=4");
        F.addImplicants(D, E);
        D.addImplicants(B, C);
        B.addImplicant(A);
        A.setValue(true);
        C.setValue(true);
        E.setValue(true);
        syst.propositions[0] = A;
        syst.propositions[1] = B;
        syst.propositions[2] = C;
        syst.propositions[3] = D;
        syst.propositions[4] = E;
        syst.propositions[5] = F;
        syst.print();
        syst.update();
        System.out.println("###########");
        syst.print();
    }

/* private */

// constructors

// instance methods

 // getters

 // setters

// static methods

}
