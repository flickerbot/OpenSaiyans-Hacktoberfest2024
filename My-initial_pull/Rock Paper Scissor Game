import java.util.Scanner;
import java.util.Random;

public class RockPaperScissors {
    
   
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        
        String[] options = {"rock", "paper", "scissors"};
        
        
        boolean playAgain = true;

       
        while (playAgain) {
           
            System.out.print("Enter your choice (rock, paper, scissors): ");
            String playerChoice = scanner.nextLine().toLowerCase();
            
           
            if (!playerChoice.equals("rock") && !playerChoice.equals("paper") && !playerChoice.equals("scissors")) {
                System.out.println("Invalid input. Please enter 'rock', 'paper', or 'scissors'.");
                continue;
            }
            
            
            String computerChoice = options[random.nextInt(3)];
            
           
            System.out.println("You chose: " + playerChoice);
            System.out.println("Computer chose: " + computerChoice);
            
           
            if (playerChoice.equals(computerChoice)) {
                System.out.println("It's a draw!");
            } else if ((playerChoice.equals("rock") && computerChoice.equals("scissors")) ||
                       (playerChoice.equals("scissors") && computerChoice.equals("paper")) ||
                       (playerChoice.equals("paper") && computerChoice.equals("rock"))) {
                System.out.println("You win!");
            } else {
                System.out.println("You lose!");
            }
            
            
            System.out.print("Do you want to play again? (yes/no): ");
            String playAgainInput = scanner.nextLine().toLowerCase();
            
            if (!playAgainInput.equals("yes")) {
                playAgain = false;
            }
        }

        System.out.println("Thanks for playing!");
        scanner.close();
    }
}
