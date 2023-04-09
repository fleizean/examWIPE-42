#pragma once

#include <iostream>
#include <string>
#include <map>

#include "ASpell.hpp"
#include "ATarget.hpp"

class Warlock
{
private:
    std::string name;
    std::string title;

    Warlock();
    Warlock(Warlock const &rhs);
    Warlock &operator=(Warlock const &rhs);
public:
    Warlock(std::string const &name, std::string const &title);
    virtual ~Warlock();

    std::string const &getName() const;
    std::string const &getTitle() const;

    void setTitle(std::string const &title);

    void introduce() const;
};