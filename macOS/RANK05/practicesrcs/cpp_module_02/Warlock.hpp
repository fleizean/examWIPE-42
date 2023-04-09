#pragma once

#include <iostream>
#include <string>
#include <map>

#include "SpellBook.hpp"
#include "ASpell.hpp"
#include "ATarget.hpp"

class Warlock
{
private:
    std::string name;
    std::string title;

    SpellBook book;

    Warlock();
    Warlock(Warlock const &rhs);
    Warlock &operator=(Warlock const &rhs);
public:
    Warlock(std::string const &name, std::string const &title);
    ~Warlock();

    std::string const &getName() const;
    std::string const &getTitle() const;

    void setTitle(std::string const &title);

    void introduce() const;

    void learnSpell(ASpell* spell);
    void forgetSpell(std::string name);
    void launchSpell(std::string name, ATarget const &target);
};