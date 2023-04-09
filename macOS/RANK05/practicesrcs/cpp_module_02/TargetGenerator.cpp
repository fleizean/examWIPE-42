#include "TargetGenerator.hpp"

TargetGenerator::TargetGenerator()
{}

TargetGenerator::~TargetGenerator()
{
    std::map<std::string, ATarget *>::iterator it_begin = this->arr.begin();
    std::map<std::string, ATarget *>::iterator it_end = this->arr.end();
    while (it_begin != it_end)
    {
        delete it_begin->second;
        ++it_begin;
    }
    this->arr.clear();
}

void TargetGenerator::learnTargetType(ATarget* target)
{
    if (target)
        arr.insert(std::pair<std::string, ATarget *>(target->getType(), target->clone()));
}

void TargetGenerator::forgetTargetType(const std::string &name)
{
    std::map<std::string, ATarget *>::iterator it = arr.find(name);
	if (it != arr.end())
		delete it->second;
    arr.erase(name);
}

ATarget* TargetGenerator::createTarget(const std::string &name)
{
    std::map<std::string, ATarget *>::iterator it = arr.find(name);
    if (it != arr.end())
        return arr[name];
    return NULL;
}
