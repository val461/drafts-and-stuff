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

public interface Proposition
{
    public String desc();
    public void setDescription(String newDescription);
    public LogicalState value();
    public boolean setValue(LogicalState truthValue);    // return true if and only if value is changed
    public boolean setValue();  // determine value automatically from implicants set using function ‘impliedBy’
    public void setImplicants(Proposition... implicants);   // must call this.setValue() at the end
    public void addImplicants(Proposition... implicants);
    public void forgetImplicants();

    default boolean isFalse()
    {
        return (this.value() == LogicalState.FALSE);
    }

    default boolean isTrue()
    {
        return (this.value() == LogicalState.TRUE);
    }

    default boolean setValue(boolean truthValue)
    {
        if (truthValue)
            return this.setValue(LogicalState.TRUE);
        else
            return this.setValue(LogicalState.FALSE);
    }

    default public void setImplicant(Proposition implicant)
    {
        this.setImplicants(implicant);
    }
    
    default public void addImplicant(Proposition implicant)
    {
        this.addImplicants(implicant);
    }
    
    default public void implies(Proposition consequent)
    {
        consequent.addImplicant(this);
    }
}

class Prop implements Proposition
{
// instance variables

    private LogicalState truthValue = LogicalState.UNCERTAIN;
    private Proposition[][] setsOfImplicants = new Proposition[0][0];
    private String description = "";

/* public */

// constructors

    public Prop() {}

    public Prop(String description)
    {
        this(LogicalState.UNCERTAIN, description);
    }

    public Prop(LogicalState truthValue)
    {
        this(truthValue, "");
    }

    public Prop(LogicalState truthValue, String description)
    {
        this.setValue(truthValue);
        this.setDescription(description);
    }

    public Prop(String description, LogicalState truthValue)
    {
        this(truthValue, description);
    }

    public Prop(Proposition... implicants)
    {
        this.setImplicants(implicants);
    }

    public Prop(Proposition[]... implicants)
    {
        this.setImplicants(implicants);
    }

// instance methods

    @Override public boolean setValue()
    {
        sets:
        for (Proposition[] set : this.setsOfImplicants)
        {
            for (Proposition implicant : set)   // check that all implicants in the set are true
            {
                if (! implicant.isTrue())
                    continue sets;
            }
            return this.setValue(LogicalState.TRUE);
        }
        return this.setValue(LogicalState.UNCERTAIN);
    }

 // getters

    @Override public LogicalState value()
    {
        return this.truthValue;
    }

    @Override public String desc()
    {
        return this.description;
    }

 // setters

    @Override public void setImplicants(Proposition... implicants)
    {
        this.setImplicants(implicants);
    }

    public void setImplicants(Proposition[]... setsOfImplicants)
    {
        this.setsOfImplicants = setsOfImplicants;
        this.setValue();
    }

    @Override public void addImplicants(Proposition... implicants)
    {
        Proposition[][] oldSetsOfImplicants = this.setsOfImplicants,
                        newSetsOfImplicants;
        int length = oldSetsOfImplicants.length;
        newSetsOfImplicants = new Proposition[length+1][];
        System.arraycopy(oldSetsOfImplicants, 0, newSetsOfImplicants, 0, length);
        newSetsOfImplicants[length] = implicants;
        this.setsOfImplicants = newSetsOfImplicants;
    }

    @Override public void forgetImplicants()
    {
        this.setsOfImplicants = new Proposition[0][0];
        this.setValue();
    }

    @Override public boolean setValue(LogicalState newValue)
    {
        LogicalState oldValue = this.truthValue;
        this.truthValue = newValue;
        return (this.value() != oldValue);
    }

    @Override public void setDescription(String newDescription)
    {
        this.description = newDescription;
    }

/* private */

// instance methods

 // getters

 // setters

// static methods

}
