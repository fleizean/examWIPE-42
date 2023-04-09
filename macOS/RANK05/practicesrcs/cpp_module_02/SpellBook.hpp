#pragma once

#include "ASpell.hpp"
#include "ATarget.hpp"
#include <string>
#include <iostream>
#include <map>

class SpellBook
{
    private:
        std::map<std::string, ASpell *> arr;

        SpellBook(SpellBook const &rhs);
        SpellBook &operator=(SpellBook const &rhs);

    public:
        SpellBook();
        ~SpellBook();

        void learnSpell(ASpell *spell);
        void forgetSpell(std::string const &name);
        ASpell* createSpell(std::string const &name);

};