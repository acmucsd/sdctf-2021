import java.io.IOException;

@FunctionalInterface
interface Challenge {
    /**
     * Runs the challenge. 
     */
    void run() throws IOException, InvalidInputException;
}
