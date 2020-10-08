package pl.edu.uwm.wmii.paweldabe.laboratorium00;

public class Main {

    public static void main(String[] args) {
        System.out.println(31 + 29 + 31);
        int liczba = 0;
        for (int i = 1; i <= 10; i++) {
            liczba += i;
        }

        System.out.println(liczba);

        int wynik =1 ;
        for (int i = 1; i<=10;i++){
            wynik=wynik*i;
        }
        System.out.println(wynik);

        int saldo =1000;
        for(int i = 0;i<=2;i++) {
            saldo += (saldo * 0.06);
        }
        System.out.println(saldo);



        }

    }



