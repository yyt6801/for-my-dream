double remainMoney=3.5;
        int remainSize=3;
        if (remainSize == 1) {
            remainSize--;
            return (double) Math.round(remainMoney * 100) / 100;
        }
        Random r = new Random();
        double min = 0.01; //
        double max = remainMoney / remainSize * 2;
        double money = r.nextDouble() * max;
        money = money <= min ? 0.01: money;
        money = Math.floor(money * 100) / 100;
        remainSize--;
        remainMoney -= money;
        double mymonry = money;
        System.out.println(mymonry);