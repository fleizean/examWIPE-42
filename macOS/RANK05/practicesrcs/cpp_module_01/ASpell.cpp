#include "ASpell.hpp"

ASpell::ASpell() : name(), effects() {}

ASpell::ASpell(std::string const &name, std::string const &effects) : name(name), effects(effects) {}

ASpell::ASpell(ASpell const &rhs) : name(rhs.name), effects(rhs.effects) {}

ASpell &ASpell::operator=(ASpell const &rhs)
{
    this->name = rhs.name;
    this->effects = rhs.effects;

    return (*this);
}

ASpell::~ASpell() {}

std::string const &ASpell::getName() const { return this->name; }
std::string const &ASpell::getEffects() const { return this->effects; }

void ASpell::launch(ATarget const &target) const
{
    target.getHitBySpell((*this));
}
