public class DogLauncher{
    
    public static void stringTest() {
        String potato = "potato";
        System.out.println("is potato identiting to potato?");
        System.out.println(potato==potato);
        
        String newPotato = new String("potato");
        System.out.println("is potato equal to newpotato?");
        System.out.println(potato.equals(newPotato));
        System.out.println("is potato identity to newpotato?");
        System.out.println(potato==newPotato);
    }
    public static void main(String[] args) {
       stringTest(); 
    }
}