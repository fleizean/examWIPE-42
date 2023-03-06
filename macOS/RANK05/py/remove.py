from genericpath import exists
from importlib.resources import path
import os, glob

# Extensions
extensions = [".cpp", ".hpp", ".txt", ".out", ".gch"]

# Practice Sources
cpp_module_00 = "practicesrcs/cpp_module_00"
cpp_module_01 = "practicesrcs/cpp_module_01"
cpp_module_02 = "practicesrcs/cpp_module_02"

# Subjects
subject_00 = """--------------------------------------------------------------------------------
Assignment name  : cpp_module_00
Expected files   : Warlock.cpp Warlock.hpp
--------------------------------------------------------------------------------

Make a Warlock class. It has to be in Coplien's form.

It has the following private attributes :
* name (string)
* title (string)

Since they're private, you will write the following getters :
* getName, returns a reference to constant string
* getTitle, returns a reference to constant string

Both these functions will have to be callable on a constant Warlock.

Create the following setter: 
* setTitle, returns void and takes a reference to constant string

Your Warlock will also have, in addition to whatever's required by Coplien's
form, a constructor that takes, in this order, its name and title. Your Warlock
will not be able to be copied, instantiated by copy, or instantiated without a
name and a title.

For example :

Warlock bob;                            //Does not compile
Warlock bob("Bob", "the magnificent");  //Compiles
Warlock jim("Jim", "the nauseating");   //Compiles
bob = jim;                              //Does not compile
Warlock jack(jim);                      //Does not compile

Upon creation, the Warlock says :

<NAME>: This looks like another boring day.

Of course, whenever we use placeholders like <NAME>, <TITLE>, etc...
in outputs, you will replace them by the appropriate value. Without the < and >.

When he dies, he says:

<NAME>: My job here is done!

Our Warlock must also be able to introduce himself, while boasting with all its
might.

So you will write the following function:
* void introduce() const;

It must display:

<NAME>: I am <NAME>, <TITLE>!

Here's an example of a test main function and its associated output:

int main()
{
  Warlock const richard("Richard", "Mistress of Magma");
  richard.introduce();
  std::cout << richard.getName() << " - " << richard.getTitle() << std::endl;

  Warlock* jack = new Warlock("Jack", "the Long");
  jack->introduce();
  jack->setTitle("the Mighty");
  jack->introduce();

  delete jack;

  return (0);
}

~$ ./a.out | cat -e
Richard: This looks like another boring day.$
Richard: I am Richard, Mistress of Magma!$
Richard - Mistress of Magma$
Jack: This looks like another boring day.$
Jack: I am Jack, the Long!$
Jack: I am Jack, the Mighty!$
Jack: My job here is done!$
Richard: My job here is done!$
~$
"""

subject_01 = """--------------------------------------------------------------------------------
Assignment name  : cpp01_02
Expected files   : Warlock.cpp Warlock.hpp
                   ASpell.hpp ASpell.cpp
				   ATarget.hpp ATarget.cpp
				   Fwoosh.hpp Fwoosh.cpp
				   Dummy.hpp Dummy.cpp
--------------------------------------------------------------------------------

In the Warlock class, the switch statement is FORBIDDEN and its use would
result in a -42.

Create an abstract class called ASpell, in Coplien's form, that has the
following protected attributes:

* name (string)
* effects (string)

Both will have getters (getName and getEffects) that return strings.

Also add a clone pure method that returns a pointer to ASpell.

All these functions can be called on a constant object.

ASpell has a constructor that takes its name and its effects, in that order.

Now you will create an ATarget abstract class, in Coplien's form. It has a type
attribute, which is a string, and its associated getter, getType, that return a
reference to constant string.

In much the same way as ASpell, it has a clone() pure method.

All these functions can be called on a constant object.

It has a constructor that takes its type.

Now, add to your ATarget a getHitBySpell function that takes a reference to
constant ASpell.

It will display :

<TYPE> has been <EFFECTS>!

<TYPE> is the ATarget's type, and <EFFECTS> is the return of the ASpell's
getEffects function.

Finally, add to your ASpell class a launch function that takes a reference to
constant ATarget.

This one will simply call the getHitBySpell of the passed object, passing the
current instance as parameter.

When all this is done, create an implementation of ASpell called Fwoosh. Its
default constructor will set the name to "Fwoosh" and the effects to
"fwooshed". You will, of course, implement the clone() method. In the case of
Fwoosh, it will return a pointer to a new Fwoosh object.

In the same way, create a concrete ATarget called Dummy, the type of which
is "Target Practice Dummy". You must also implement its clone() method.

Add to the Warlock the following member functions:

* learnSpell, takes a pointer to ASpell, that makes the Warlock learn a spell
* forgetSpell, takes a string corresponding a to a spell's name, and makes the
  Warlock forget it. If it's not a known spell, does nothing.
* launchSpell, takes a string (a spell name) and a reference to ATarget, that
  launches the spell on the selected target. If it's not a known spell, does
  nothing.

You will need a new attribute to store the spells your Warlock knows. Several
types fit the bill, it's up to you to choose the best one.

Below is a possible test main and its expected output:

int main()
{
  Warlock richard("Richard", "the Titled");

  Dummy bob;
  Fwoosh* fwoosh = new Fwoosh();

  richard.learnSpell(fwoosh);

  richard.introduce();
  richard.launchSpell("Fwoosh", bob);

  richard.forgetSpell("Fwoosh");
  richard.launchSpell("Fwoosh", bob);
}

~$ ./a.out | cat -e
Richard: This looks like another boring day.$
Richard: I am Richard, the Titled!$
Target Practice Dummy has been fwooshed!$
Richard: My job here is done!$
"""

subject_02 = """--------------------------------------------------------------------------------
Assignment name  : cpp_module_02
Expected files   : Warlock.cpp Warlock.hpp
                   ASpell.hpp ASpell.cpp
				   ATarget.hpp ATarget.cpp
				   Fwoosh.hpp Fwoosh.cpp
				   Dummy.hpp Dummy.cpp
				   Fireball.hpp Fireball.cpp
				   Polymorph.hpp Polymorph.cpp
				   BrickWall.hpp BrickWall.cpp
				   SpellBook.hpp SpellBook.cpp
				   TargetGenerator.hpp TargetGenerator.cpp
--------------------------------------------------------------------------------

In the Warlock, SpellBook and TargetGenerator classes, the switch statement is
FORBIDDEN and its use would result in a -42.

Create the following two spells, on the same model as Fwoosh:

* Fireball (Name: "Fireball", Effects: "burnt to a crisp")
* Polymorph (Name: "Polymorph", Effects: "turned into a critter")

In addition to this, just so he won't have only dummy to attack, let's make a
new target for him, which will be the BrickWall (Type: "Inconspicuous Red-brick Wall").

Now, make a SpellBook class, in canonical form, that can't be copied or instantiated
by copy. It will have the following functions:

* void learnSpell(ASpell*), that COPIES a spell in the book
* void forgetSpell(string const &), that deletes a spell from the book, except
  if it isn't there
* ASpell* createSpell(string const &), that receives a string corresponding to
  the name of a spell, creates it, and returns it.

Modify the Warlock, now, make it have a spell book that will be created with
him and destroyed with him. Also make his learnSpell and forgetSpell functions
call those of the spell book.

The launchSpell function will have to use the SpellBook to create the spell
it's attempting to launch.

Make a TargetGenerator class, in canonical form, and as before,
non-copyable.

It will have the following functions:

* void learnTargetType(ATarget*), teaches a target to the generator

* void forgetTargetType(string const &), that makes the generator forget a
  target type if it's known

* ATarget* createTarget(string const &), that creates a target of the
  specified type

Phew, that's done. Now here's a test main. It's not very thorough, so make sure 
to use your own aswell.

int main()
{
  Warlock richard("Richard", "foo");
  richard.setTitle("Hello, I'm Richard the Warlock!");
  BrickWall model1;

  Polymorph* polymorph = new Polymorph();
  TargetGenerator tarGen;

  tarGen.learnTargetType(&model1);
  richard.learnSpell(polymorph);

  Fireball* fireball = new Fireball();

  richard.learnSpell(fireball);

  ATarget* wall = tarGen.createTarget("Inconspicuous Red-brick Wall");

  richard.introduce();
  richard.launchSpell("Polymorph", *wall);
  richard.launchSpell("Fireball", *wall);
}

~$ ./a.out | cat -e
Richard: This looks like another boring day.$
Richard: I am Richard, Hello, I'm Richard the Warlock!!$
Inconspicuous Red-brick Wall has been turned into a critter!$
Inconspicuous Red-brick Wall has been burnt to a crisp!$
Richard: My job here is done!$
~$
"""

create_subject00 = r"practicesrcs/cpp_module_00/subject.en.txt"
create_subject01 = r"practicesrcs/cpp_module_01/subject.en.txt"
create_subject02 = r"practicesrcs/cpp_module_02/subject.en.txt"

def module_00_reset():
    dosyalar = os.listdir(cpp_module_00)
    for dosya in dosyalar:
      dosya_adi, dosya_uzantisi = os.path.splitext(dosya)
      if dosya_uzantisi in extensions:
          dosya_yolu = os.path.join(cpp_module_00, dosya)
          os.remove(dosya_yolu)
          print(f"{dosya} silindi.")
    os.system("clear")
    file = open(create_subject00, "w")
    file.write(subject_00)
    file.close()
    print("Module_00 başarılı şekilde resetlendi.")

def module_01_reset():
    dosyalar = os.listdir(cpp_module_01)
    for dosya in dosyalar:
      dosya_adi, dosya_uzantisi = os.path.splitext(dosya)
      if dosya_uzantisi in extensions:
          dosya_yolu = os.path.join(cpp_module_01, dosya)
          os.remove(dosya_yolu)
          print(f"{dosya} silindi.")
    os.system("clear")
    file = open(create_subject01, "w")
    file.write(subject_01)
    file.close()
    print("Module_01 başarılı şekilde resetlendi.")

def module_02_reset():
    dosyalar = os.listdir(cpp_module_02)
    for dosya in dosyalar:
      dosya_adi, dosya_uzantisi = os.path.splitext(dosya)
      if dosya_uzantisi in extensions:
          dosya_yolu = os.path.join(cpp_module_02, dosya)
          os.remove(dosya_yolu)
          print(f"{dosya} silindi.")
    os.system("clear")
    file = open(create_subject02, "w")
    file.write(subject_02)
    file.close()
    print("Module_02 başarılı şekilde resetlendi.")

def subjects_reset():
  file1 = open(create_subject00, "w")
  file1.write(subject_00)
  file1.close()

  file2 = open(create_subject01, "w")
  file2.write(subject_01)
  file2.close()

  file3 = open(create_subject02, "w")
  file3.write(subject_02)
  file3.close()
  print("Subjectler başarılı şekilde oluşturuldu.")
while(1):
    os.system("clear")
    print("----------- examWIPE -----------")
    print("1- Module_00'ı resetle")
    print("2- Module_01'ı resetle")
    print("3- Module_02'ı resetle")
    print("4- Hepsini resetle")
    print("5- Subject dosyalarını oluştur")
    print("6- Exit")
    print("--------------------------------")
    secim = input("Seçim Numarınızı Giriniz: ")
    
    if secim == "1":
        module_00_reset()
    elif secim == "2":
        module_01_reset()
    elif secim == "3":
        module_02_reset()
    elif secim == "4":
        module_00_reset()
        module_01_reset()
        module_02_reset()
    elif secim == "5":
        subjects_reset()
    elif secim == "6":
        exit()
    else:
        print("Yanlış seçim numarası girdiniz.")
        exit()


