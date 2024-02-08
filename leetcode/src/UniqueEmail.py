class UniqueEmail:

    def cleanUpEmail(email: list()) -> set:
        result = set()
        for i in range(0, len(email)):
            tempString = ""
            local, domain = email[i].split("@")
            for element in email[i]:
                if(element == '.'):
                    continue
                elif(element == '+'):
                    break
                else:
                    tempString += element

            finalString = f"{tempString}@{domain}"
            result.add(finalString)

        return result


    email = [
        "test.email+alex@leetcode.com",
        "test.e.mail+bob.cathy@leetcode.com",
        "testemail+david@lee.tcode.com"]
    print(cleanUpEmail(email))