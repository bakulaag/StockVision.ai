// #include <iostream>
// using namespace std;

// class Shape {
// public:
//     // Pure virtual function
//     virtual double area()  = 0;
   

//     // Regular member function
//     void display()  {
//         cout << "This is a shape." << endl;
//     }
// };

// class Rectangle : public Shape {
// private:
//     double width;
//     double height;

// public:
//     static int x;
//      static void displayCount() {
//         cout << "Count: " << x << endl;
//     }

//     Rectangle(double width, double height) {
//         this->width = width;
//         this->height = height;
//     }

//     double area()   {
//         return width * height;
//     }
// };

// class Circle : public Shape {
// private:
//     double radius;

// public:
//     Circle(double radius) {
//         this->radius = radius;
//     }

//     double area()   {
//         return 3.14159 * radius * radius;
//     }
// };
// int Rectangle::x = 0;
// int main() {
//     // Shape* shape1 = new Rectangle(10, 20);
//     Rectangle shape1(1,20);
//     Shape* shape2 = new Circle(5);
//     Rectangle::displayCount();
//     cout << "Area of rectangle: " << shape1.area() << endl;
//     cout << "Area of circle: " << shape2->area() << endl;

//     // delete shape1;
//     delete shape2;

//     return 0;
// }
#include <iostream>
using namespace std;

class A {
public:
    void show() {
        cout << "Class A" << endl;
    }
};

class B : virtual public A {
};

class C : virtual public A {
    public:
    void show()
    {
        cout<<"Class C"<<endl;
    }
};

class D : public B, public C {
};

int main() {
    D d;
    d.show();  // This will cause an ambiguity error
    return 0;
}


// #include <iostream>
// using namespace std;

// class A {
// public:
//     A() {
//         cout << "Constructor of A" << endl;
//     }
//     void show() {
//         cout << "Class A" << endl;
//     }
// };

// class B : virtual public A {
// public:
//     B() {
//         cout << "Constructor of B" << endl;
//     }
// };

// class C : virtual public A {
// public:
//     C() {
//         cout << "Constructor of C" << endl;
//     }
// };

// class D : public B, public C {
// public:
//     D() {
//         cout << "Constructor of D" << endl;
//     }
// };

// int main() {
//     D d;
//     d.show();  // This will work correctly
//     return 0;
// }
