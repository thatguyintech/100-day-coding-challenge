public class Accumul {
    
    public static String accum(String s) {
        StringBuilder newString = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            char currentChar = s.charAt(i);
            newString.append(Character.toUpperCase(currentChar));
            for (int j = 0; j < i; j++) {
                newString.append(Character.toLowerCase(currentChar));
            }
            if (i != s.length() - 1) {
                newString.append("-");
            }
        }
        return newString.toString();
    }
}