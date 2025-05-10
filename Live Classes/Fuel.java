import java.util.Scanner;

public class Fuel{
	public static void main(String... args){
	Scanner input = new Scanner(System.in);

	double amountOfFuel = 0;

	System.out.print("What is your budget? ");
	int budget = input.nextInt();

	final int price_Per_Litre = 855;

	amountOfFuel = (double) budget / price_Per_Litre;

	System.out.println();
	System.out.printf("You can afford %.2f litres of fuel", amountOfFuel);
	System.out.println();

}}