import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigDecimal;
import java.util.regex.Pattern;

import javax.lang.model.SourceVersion;

import jdk.jshell.JShell;
import jdk.jshell.Snippet.Status;

public class AlternativeArithmetic {
    // Set this to TRUE when deploying this challenge!
    // private static final boolean DEPLOY = false;
    private static final String INTERMEDIATE_FLAG = "sdctf{JAVA_Ar1thm3tIc_15_WEirD}";
    private static final String FINAL_FLAG = "sdctf{MATH_pr0f:iS_tH1S_@_bUG?CS_prOF:n0P3_tHIS_iS_A_fEATuRe!}";
    // private static final int EXIT_PARTICIPANT_ERROR = 0;
    // private static final int EXIT_INTERNAL_ERROR = 2;
    private static BufferedReader input;
    
    // Internal error logging
    // (deprecated, instead redirect standard error to somewhere the participant cannot see, preferably appending that to a log file)
    // Ex. `java AlternativeArithmetic 2>> err.log`
    // private static final String ERR_LOG_FILE = "alt-arithmetic-errors.log";

    private static void die(String reason) throws InvalidInputException {
        System.out.println(reason);
        // System.exit(EXIT_PARTICIPANT_ERROR);
        throw new InvalidInputException();
    }
    
    private static void wrongAnswer() throws InvalidInputException {
        die("Sorry, your answer is not correct. Try something else next time.");
    }

    private static void correctAnswer() {
        // TODO: different message each time?
        System.out.println("Perfect! You are correct.");
    }

    private static void invalidAnswer() throws InvalidInputException {
        die("Sorry, your answer (or any part of your answer) is not in a valid format. Read the question carefully.\n" +
            "If a number is asked, it may either be invalid or overflows the bound for a type.");
    }

    private static String promptInput(String prompt) throws IOException {
        System.out.print(prompt);
        System.out.flush();
        return input.readLine();
    }

    private static void challenge1() throws IOException, InvalidInputException {
        System.out.println("1. Find a nonzero `long x` such that `x == -x`, enter numbers only, no semicolons:");
        // System.out.print("1. Find a nonzero `long x` such that `x == -x`, enter numbers only, no semicolons:\nx = ");
        // System.out.flush();
        try {
            long x = Long.parseLong(promptInput("x = "));
            // long x = Long.parseLong(input.readLine());
            // The only correct answer: -9223372036854775808, or Long.MIN_VALUE
            if (x != 0 && x == -x) {
                correctAnswer();
            } else {
                wrongAnswer();
            }
        } catch (NumberFormatException e) {
            invalidAnswer();
        }
    }

    private static boolean distanceLessThan(long x, long y, long maxAbs) {
        // overflow resistant checking
        try {
            long signedDifference = Math.subtractExact(x, y);
            // Using Math.abs instead will make this check vulnerable to the same attack as challenge 1
            // Since Math.abs(Long.MIN_VALUE) = Long.MIN_VALUE
            return (-maxAbs <= signedDifference && signedDifference <= maxAbs);
        } catch (ArithmeticException e) {
            // overflow
            return false;
        }
    }

    private static void challenge2() throws IOException, InvalidInputException {
        System.out.println("2. Find 2 different `long` variables `x` and `y`, differing by at most 10, such that `Long.hashCode(x) == Long.hashCode(y)`:");
        // Solution: (x,y) being any pair (order does not matter) among (0,-1), (1,-2), (2,-3), ...
        try {
            long x = Long.parseLong(promptInput("x = ")), y = Long.parseLong(promptInput("y = "));
            if (x == y) {
                die("In your input, x == y");
            }
            if (!distanceLessThan(x, y, 10)) {
                die("The numbers differ by more than 10");
            }
            if (Long.hashCode(x) == Long.hashCode(y)) {
                correctAnswer();
            } else {
                // wrongAnswer();
                die("The hashes are not equal: Long.hashCode(x) != Long.hashCode(y)");
            }
        } catch (NumberFormatException e) {
            invalidAnswer();
        }
    }

    private static boolean isLucky(float magic) {
        int iter = 0;
        for (float start = magic; start < (magic + 256); start++) {
            if ((iter++) > 2048) {
                return true;
            }
        }
        return false;
    }

    private static final String IS_LUCKY_SRC =
        "boolean isLucky(float magic) {\n" + 
        "    int iter = 0;\n" + 
        "    for (float start = magic; start < (magic + 256); start++) {\n" + 
        "        if ((iter++) > 2048) {\n" + 
        "            return true;\n" + 
        "        }\n" + 
        "    }\n" + 
        "    return false;\n" + 
        "}";

    // private static boolean roulette(float seed) {
    //     for (float start = seed; start < (seed + 256); start++) {
    //         //
    //     }
    // }

    private static void challenge3() throws IOException, InvalidInputException {
        System.out.println("3. Enter a `float` value `f` that makes the following function return true:");
        System.out.println(IS_LUCKY_SRC);
        try {
            String input = promptInput("f = ");
            if (input.length() > 7) {
                die("Your input must be less than 7 characters long (excluding newlines).");
            }
            float userInput = Float.parseFloat(input);
            if (input.contains("x") || input.contains("X")) {
                // This is to prevent participants from using HexFloatingPointLiteral to possibly work around the character limit
                // See https://docs.oracle.com/en/java/javase/15/docs/api/java.base/java/lang/Double.html#valueOf(java.lang.String)
                die("You cannot use the letter 'x' either in lowercase or uppercase in your input.");
            }
            if (isLucky(userInput)) {
                correctAnswer();
            } else {
                wrongAnswer();
            }
        } catch (NumberFormatException e) {
            invalidAnswer();
        }
    }

    private static void challenge4() throws IOException, InvalidInputException {
        System.out.println(
            "4. Enter 3 `String` values `s1`, `s2`, and `s3` such that:\n" +
            "new BigDecimal(s1).add(new BigDecimal(s2)).compareTo(new BigDecimal(s3)) == 0\n" +
            "but\n" +
            "Double.parseDouble(s1) + Double.parseDouble(s2) != Double.parseDouble(s3)\n" +
            "Do not enter quotation marks."
        );
        try {
            String s1 = promptInput("s1 = "), s2 = promptInput("s2 = "), s3 = promptInput("s3 = ");
            // sample solutions:
            // 0.1 0.2 0.3
            // 0.1 0.7 0.8
            // 0.2 0.4 0.6
            // 0.2 0.7 0.9
            if (new BigDecimal(s1).add(new BigDecimal(s2)).compareTo(new BigDecimal(s3)) == 0 &&
                    // using == or != to compare double is BAD! Loss of precision!
                    Double.parseDouble(s1) + Double.parseDouble(s2) != Double.parseDouble(s3)) {
                correctAnswer();
            } else {
                wrongAnswer();
            }
        } catch (NumberFormatException e) {
            invalidAnswer();
        }
    }

    // Avoid RCE by filtering characters
    private static final String NUMBER_REGEX = "[0-9]*\\.?[0-9]*";
    private static final Pattern NUMBER_PATTERN = Pattern.compile(NUMBER_REGEX);
    // private static final String CHAL5_CODE1 = "var i = (%1$s) %2$s; var j = (%1$s) %3$s;";
    private static final String CHAL5_CODE1_VAR = "var %s = (%s) %s;";
    private static final String CHAL5_CODE2 = "i < j || i == j || i > j";
    // Emoji https://emojipedia.org/musical-notes/, encoded using backslash u to make it compile correctly even on Windows/non-UTF8 systems
    private static final String MUSIC_CHAR = "\ud83c\udfb6";

    private static String inputNumString(String prompt) throws IOException, InvalidInputException {
        String numString = promptInput(prompt);
        if (numString.isEmpty() || !NUMBER_PATTERN.matcher(numString).matches()) {
            die(numString + " does not match the regex " + NUMBER_REGEX);
        }
        return numString;
    }

    // May return null on error or no value returned (void)
    private static String checkEval(JShell js, String code) throws InvalidInputException {
        var events = js.eval(code);
        String value = null;
        for (var event : events) {
            if (event.status() != Status.VALID) {
                die("Invalid Java code (try running this on a Java compiler first):\n" + code);
            }
            value = event.value();
        }
        return value;
    }

    private static void challenge5() throws IOException, InvalidInputException {
        System.out.println(
            "5. Final question! [" + MUSIC_CHAR + "BOSS MUSIC" + MUSIC_CHAR + "]\n" +
            "Fill in <type>, <num1>, <num2> below:\n" +
            "var i = (<type>) <num1>; var j = (<type>) <num2>;\n" +
            "such that after running the code above, the following expression:\n" +
            "i < j || i == j || i > j\n" +
            "evaluates to `false`.\n" +
            "<num1> and <num2> are Java code that satisfies this regex: " + NUMBER_REGEX
        );
        String type = promptInput("<type>: ");
        if (!SourceVersion.isIdentifier(type)) {
            // Avoid RCE by filtering characters so that only valid identifiers are allowed
            die("`" + type + "` cannot be a valid Java type");
        }
        String num1 = inputNumString("<num1>: "), num2 = inputNumString("<num2>: ");
        System.out.println("Executing statement. Please wait...");
        System.out.flush();
        try (var js = JShell.create()) {
            // checkEval(js, String.format(CHAL5_CODE1, type, num1, num2));
            checkEval(js, String.format(CHAL5_CODE1_VAR, "i", type, num1));
            checkEval(js, String.format(CHAL5_CODE1_VAR, "j", type, num2));
            if ("false".equals(checkEval(js, CHAL5_CODE2))) {
                correctAnswer();
            } else {
                wrongAnswer();
            }
        }
    }

    private static void intermission() {
        System.out.println("Good job. You earned the intermediate flag:");
        System.out.println(INTERMEDIATE_FLAG);
        System.out.println("To get the final flag please answer 2 more questions.");
    }

    private static void win() {
        System.out.println("Congratulations, hax0r. You deserve the final flag:");
        System.out.println(FINAL_FLAG);
    }

    private static final Challenge[] CHALLENGES = {
        AlternativeArithmetic::challenge1,
        AlternativeArithmetic::challenge2,
        AlternativeArithmetic::challenge3,
        AlternativeArithmetic::intermission,
        AlternativeArithmetic::challenge4,
        AlternativeArithmetic::challenge5,
    };

    private static void run() throws IOException {
        input = new BufferedReader(new InputStreamReader(System.in));
        System.out.println("Welcome to the 1337 Java quiz!\n"
            + "Make sure you learn its quirks before you start this journey.\n"
            + "Answer all questions to the best of your ability. Do not input any semicolons.\n"
            + "Good luck!\n");
        // challenge1();
        // challenge2();
        // challenge3();
        // intermission();
        // challenge4();
        // challenge5();
        for (Challenge challenge : CHALLENGES) {
            boolean invalidAnswer;
            do {
                invalidAnswer = false;
                try {
                    System.out.println();
                    challenge.run();
                } catch (InvalidInputException e) {
                    // Run the same challenge again to give the participant
                    // another chance
                    invalidAnswer = true;
                }
            } while (invalidAnswer);
        }
        win();
    }

    public static void main(String[] args) throws IOException {
        run();
        // // default: deploy mode (as in challenges served to the participant)
        // if (args.length >= 1 && (args[0].equals("--debug") | args[0].equals("-d"))) {
        //     System.err.println("**** Note: Running in debug mode. Stack traces will be dumped if an exception occurred ****");
        //     run();
        //     return;
        // }
        // // todo: open file in append mode
        // try (var errLog = new PrintWriter(ERR_LOG_FILE)) {
        //     try {
        //         run();
        //     } catch (Throwable error) {
        //         // avoid dumping the stack trace to the participant (and giving out hints) since this challenge is supposed
        //         // to be closed source
        //         error.printStackTrace(errLog);
        //         if (errLog.checkError()) {
        //             System.out.println("Something went wrong and this error is unable to be logged.\n" +
        //                 "Please contact an admin immediately.");
        //             System.exit(EXIT_INTERNAL_ERROR);
        //         }
        //         System.out.println("Something went wrong and this error is logged.\n" +
        //             "Please contact an admin about this.");
        //         System.exit(EXIT_INTERNAL_ERROR);
        //     }
        // }
    }
}
