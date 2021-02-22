import java.util.*;

public class Main
{
	/**
	 * Premise: In a valid statement, you won't find a ')' without already having found a (
	 * @param args
	 */
	public static void main(String args[])
	{
		if(args[0] == "" || args[0] == null)
		{
			System.exit(0);
		}
		
		final String lispString = args[0];
		
		stackHelper(lispString);
		
	}
	
	private static void stackHelper(String lispString) throws EmptyStackException
	{
		Stack<Character> lispStack = new Stack<Character>();
		
		for(char c : lispString.toCharArray())
		{
			System.out.println(c);
			if(c == '(')
			{
				System.out.println("Pushed a " + lispStack.push(c));
			}
			else if(c == ')')
			{
				System.out.println("Found a )");
				if(!lispStack.isEmpty())
				{
					if(lispStack.peek() == '(')
					{
						System.out.println("Popped a " + lispStack.pop());
					}
				}
				else
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