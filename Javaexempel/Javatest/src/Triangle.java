import java.util.*; // Scanner , Locale

class Triangle {
	public static boolean e = true;
	public static Scanner in = new Scanner(System.in);

	public static void main(String[] args) {
		int choice;
		in.useLocale(Locale.US);
		do {
			System.out
					.println("1. Area Calculations\n2. Circumference Calculations\n3. Bisector Calculations\n4. Incircle Calculations\n5. Quit\n");
			System.out
					.println("Make a choice in the menu by entering a number: ");
			choice = in.nextInt();
			Triangle.Input(choice);
		} while (e);
	}

	public static double Area(double a, double b, double c) {
		double s = (a + b + c) / 2.0;
		double d = Math.pow((s * (s - a) * (s - b) * (s - c)), 0.5);
		return d;
	}

	public static double Incircle(double a, double b, double c) {
		double are = Triangle.Area(a, b, c);
		double cir = Triangle.Circumference(a, b, c);
		double d = 2.0 * are / cir;
		return d;
	}

	public static double Circumference(double a, double b, double c) {
		double d = a + b + c;
		return d;
	}

	public static double Bisector(double b, double c, double alpha) {
		double p = 2.0 * b * c * Math.cos(alpha / 2.0);
		double bis = p / (b + c);
		return bis;
	}

	public static void Turnoff() {
		Triangle.e = false;
	}

	public static void Input(int choice) {
		switch (choice) {
		case 1:
			System.out.println("Enter all of your triangles sides: ");
			double[] area = new double[3];
			try {
				for (int i = 0; i < area.length; i++) {
					area[i] = Triangle.in.nextDouble();
				}
			} catch (IndexOutOfBoundsException o) {
				System.out.println("Too many sides entered.");
			}
			double aread = Triangle.Area(area[0], area[1], area[2]);
			System.out.println("Your triangles area is: " + aread + "\n");
			break;
		case 2:
			System.out.println("Enter all of your triangles sides: ");
			double[] circ = new double[3];
			try {
				for (int i = 0; i < circ.length; i++) {
					circ[i] = Triangle.in.nextDouble();
				}
			} catch (IndexOutOfBoundsException o) {
				System.out.println("Too many sides entered.");
			}
			double circu = Triangle.Circumference(circ[0], circ[1], circ[2]);
			System.out.println("Your triangles circumference is: " + circu
					+ "\n");
			break;
		case 3:
			System.out.println("Enter the two sides: ");
			double[] bis = new double[2];
			try {
				for (int i = 0; i < bis.length; i++) {
					bis[i] = Triangle.in.nextDouble();
				}
			} catch (IndexOutOfBoundsException o) {
				System.out.println("Too many sides entered.");
			}
			System.out.println("Enter the angle between the sides: ");
			double angle = Triangle.in.nextDouble();
			double bisu = Triangle.Bisector(bis[0], bis[1], angle);
			System.out.println("Your bisectors length is: " + bisu + "\n");
			break;
		case 4:
			System.out.println("Enter the three sides of the triangle: ");
			double[] side = new double[3];
			try {
				for (int i = 0; i < side.length; i++) {
					side[i] = Triangle.in.nextDouble();
				}
			} catch (IndexOutOfBoundsException o) {
				System.out.println("Too many sides entered.");
			}
			double incircle = Triangle.Incircle(side[0], side[1], side[2]);
			System.out.println("Your incircle has a radius of " + incircle
					+ "\n");
			break;
		case 5:
			in.close();
			Triangle.Turnoff();
		}
	}
}