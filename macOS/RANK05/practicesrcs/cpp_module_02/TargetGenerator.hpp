#pragma once

#include "ATarget.hpp"
#include <map>

class TargetGenerator
{
    private:
        std::map<std::string, ATarget *> arr;

        TargetGenerator(TargetGenerator const &rhs);
        TargetGenerator &operator=(TargetGenerator const &rhs);

    public:
        TargetGenerator();
        ~TargetGenerator();

        void learnTargetType(ATarget *target);
        void forgetTargetType(std::string const &name);
        ATarget* createTarget(std::string const &name);
};