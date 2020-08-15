int Z;

void f()
{
        int a, b, c,x;
        a = Z;
        if (a < 10) {
                b = 5;
                c = 17;
        } else {
                b = 6;
                c = 20;
                if (a == 0) {
                        c = 0;
                }
        }
        Z = b * 10 + c;
        x=a?b:c;

}

