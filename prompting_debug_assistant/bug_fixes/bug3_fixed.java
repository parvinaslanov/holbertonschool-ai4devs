import java.util.List;
import java.util.ArrayList;

public class UserLookup {
    /**
     * Intended Behavior: Find a user profile name by ID and return its length.
     * Issue Type: Runtime Exception (NullPointerException)
     */
    public static int getUserNameLength(List<String> userDatabase, int userId) {
        if (userId < 0 || userId >= userDatabase.size()) {
            return -1;
        }
        String name = userDatabase.get(userId);
        if (name == null) {
            return 0;
        }
        return name.length();
    }
}
