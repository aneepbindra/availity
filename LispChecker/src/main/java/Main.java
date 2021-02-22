import java.util.*;

public class Main
{
	/**
	 * Premise: In a valid statement, you won't find a ')' without already having found a '('
	 * 
	 * Given the premise, every time we find a ')' in the string, we look to see if we have a '('
	 * on our stack. If we do, we pop it. At the end of traversal, the stack should be empty.
	 * @param args A string in lisp (i.e, "(hello world(test))"
	 */
	public static void main(String args[])
	{
		// basic args check
		if(args[0] == "" || args[0] == null)
		{
			System.exit(0);
		}
		
		final String lispString = args[0];
		
		stackHelper(lispString);
		
	}
	
	/**
	 * Main function to loop through the given string, adding '(''s to the stack and popping
	 * when a ')' is encountered
	 * @param lispString
	 * @throws EmptyStackException
	 */
	private static void stackHelper(String lispString) throws EmptyStackException
	{
		Stack<Character> lispStack = new Stack<Character>();
		
		for(char c : lispString.toCharArray())
		{
			if(c == '(')
			{
				lispStack.push(c);
			}
			else if(c == ')')
			{
				if(!lispStack.isEmpty())
				{
					lispStack.pop();

				}
				else // we found a ')' that did not have an opening '('
				{
					failCase();
				}

			}
			
		}
		
		if(lispStack.isEmpty())
		{
			passCase();
		}
		else
		{
			failCase();
		}
	}
	
	
	
	private static void failCase()
	{
		System.out.println("The ()'s in this statement DO NOT match");
		System.exit(0);
	}
	
	private static void passCase()
	{
		System.out.println("The ()'s in this statement match!");
	}
}