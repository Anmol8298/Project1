import java.util.Scanner;
class Account 
{
	private int balance;
	Account(int balance)
	{
		this.balance=balance;
	}
	int getBalance()
	{
		return this.balance;
	}
	void Withdraw(int amount)
	{
		if(balance>=amount)
		{
			this.balance =this.balance-amount;
		}
		else
		{
			System.out.println("You insufficient balance");
		}
	}
	void Deposit(int amount)
	{
		this.balance=this.balance+amount;
}
}
		class Bank3
		{
	public static void main(String[] args) 
	{
		Scanner obj=new Scanner(System.in);
		int amount=obj.nextInt();
		System.out.println("Enter your account balance:");
		Account s = new Account(amount);
		//calling amount in balance
		System.out.println(s.getBalance());
		System.out.println("Enter amount to withdraw");
		int a =obj.nextInt();
		s.Withdraw(a);
		System.out.println("Your transaction is successfull and your current balance:"+s.getBalance());
		System.out.println("Enter amount how much you want to deposit");
		int b=obj.nextInt();
		s.Deposit(b);
		System.out.println("Your current balance is:"+s.getBalance());

	}
}
