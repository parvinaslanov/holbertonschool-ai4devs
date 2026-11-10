import java.util.ArrayList;
import java.util.List;

public class Bug3Fixed {

    // Intended: Remove all odd numbers from an ArrayList
    public static void removeOddNumbers(List<Integer> numbers) {
        // Fix: Use removeIf to safely filter elements without index drift
        numbers.removeIf(n -> n % 2 != 0);
    }

    // Intended: Compare two user account strings for equality
    public static boolean checkAccountName(String inputName, String targetName) {
        // Fix: Use .equals() for value comparison rather than reference check (==)
        if (inputName == null) return targetName == null;
        return inputName.equals(targetName);
    }

    public static void main(String[] args) {
        List<Integer> list = new ArrayList<>();
        list.add(1);
        list.add(3);
        list.add(4);
        list.add(5);
        
        removeOddNumbers(list);
        System.out.println("Filtered List: " + list);

        String name1 = new String("admin");
        String name2 = new String("admin");
        System.out.println("Names Match: " + checkAccountName(name1, name2));
    }
}
