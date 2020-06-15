import java.util.Random;
public class random_money {
    public static void main(String[] args) {
        System.out.println("welcome to wechat_redPackage!");
        double remainMoney=5;//
        int remainSize=10;//
        int i=1;
        while (remainSize > 1) {
        Random r = new Random();
        double min = 0.01; //
        double max = remainMoney / remainSize * 2;
        double money = r.nextDouble() * max;
        money = money <= min ? 0.01: money;
        money = Math.floor(money * 100) / 100;
        remainSize--;
        remainMoney -= money;
        double mymonry = money;
        System.out.println(i+":   "+mymonry);
        i++;
        if (remainSize == 1) {
        remainSize--;
        System.out.println("last: "+(double) Math.round(remainMoney * 100) / 100);
        break;
        }
        }
    }
}