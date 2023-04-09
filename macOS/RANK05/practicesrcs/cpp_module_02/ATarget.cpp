#include "ATarget.hpp"

ATarget::ATarget() : type() {}

ATarget::ATarget(std::string const &type) : type(type) {}

ATarget::ATarget(ATarget const &rhs) : type(rhs.type) {}

ATarget &ATarget::operator=(ATarget const &rhs)
{
    this->type = rhs.type;

    return (*this);
}

ATarget::~ATarget() {}

std::string const &ATarget::getType() const { return this->type; }

void ATarget::getHitBySpell(ASpell const &spell) const
{
    std::cout << this->type << " has been " << spell.getEffects() << "!\n";
}