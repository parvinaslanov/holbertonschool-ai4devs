import java.util.List;
import java.util.ArrayList;

public class UserLookup {
    /**
     * Intended Behavior: Find a user profile name by ID and return its length.
     * Issue Type: Runtime Exception (NullPointerException)
     */
    public static int getUserNameLength(List<String> userDatabase, int userId) {
        String name = userDatabase.get(userId);
        
        // Bug: Doesn't check if 'name' is null before calling .length()
        return name.length();
    }
}
