import requests


def submit():
    url = 'http://yxhg.yzjyy.com/api/SurveyQuestionAuthenticated/CreateSubmitQuestion?tenantCode=yzjcsdev&surveyId=56f33fd8-3334-4f40-8611-d536b3bea54b'
    content = {
        "survey_result_id": "ee993c9c-fbbe-4b60-b185-bbcc9c05ac0f",
        "answerList": [
            {
                "questionId": "76aa3185-f719-4dce-b7aa-b280c0a20768",
                "optionIds": "b0c4fb13-7675-4e7b-94e4-8106b54d435b,",
                "remark": ""
            },{
                "questionId": "53ffa822-67ff-48c8-a89e-de73dfcbe7aa", 
                "optionIds": "20c88ca2-d43c-42ac-9365-678af1715edc,", 
                "remark": ""
            }, {
                "questionId": "53000cff-25af-433a-a832-dd6df556a4a1", 
                "optionIds": "f38de01d-17ea-4c6a-b821-fc36af5d3616,", 
                "remark": ""
            }, {
                "questionId": "c42c9363-5a17-4b76-a41e-0b171b0add3a", 
                "optionIds": "7d438a67-d91d-4ea1-9c71-0dac3c0fcaed,", 
                "remark": ""
            }, {
                "questionId": "be355af2-f1ad-46b7-9c51-e00bb6fdfbfa", 
                "optionIds": "a52fc796-99e3-41e3-8798-ff9b957ee365,", 
                "remark": ""
            }, {
                "questionId": "429cbc23-da96-4f64-810a-b9ea550d76dc", 
                "optionIds": "a344db9a-c7ce-428f-a2d7-879997307f5f,", 
                "remark": ""
            }, {
                "questionId": "1901a592-6be8-4d1f-a2bc-604b0e74b739", 
                "optionIds": "67a3334d-aa24-4bcc-949d-85d020870a78,", 
                "remark": ""
            }, {
                "questionId": "e5e9949e-c225-4ef1-9865-f0cc254afb26", 
                "optionIds": "8d4d2a42-7f0e-417a-945c-6cd2d3ba0546,", 
                "remark": ""
            }, {
                "questionId": "1a4b5d50-7666-4764-af6f-30862aa39e49", 
                "optionIds": "fabcac09-cf5f-41b3-bc0c-57825077695a,", 
                "remark": ""
            }, {
                "questionId": "d2f4fb76-8675-4b09-8902-f8b303ff560d", 
                "optionIds": "ffe85c8a-ed24-4463-b965-55005c60328c,", 
                "remark": ""
            }
        ], 
        "sign_companyid": "92097275-32a5-45da-9a67-f95486a67ea0", 
        "ownerid": "e89e451e-f89e-4487-9bad-4ae05894b3cc", 
        "survey_repost_id": "e9a10972-3759-432d-8dd9-82b04cf665eb",
    }

    x = requests.post(url, data=content)
    print(x.text)


def get_survey():
    url = url = 'http://yxhg.yzjyy.com//debug/vue/static/js/59.757f825bd12afd27c084.js'
    x = requests.get(url=url)
    print(x.text)



if __name__ == '__main__':
    # get_survey()
    submit()

# http://yxhg.yzjyy.com//debug/vue/index.html
#/surveyResultList/
# 56f33fd8-3334-4f40-8611-d536b3bea54b/ surveyId
# e89e451e-f89e-4487-9bad-4ae05894b3cc/ ownerid
# 92097275-32a5-45da-9a67-f95486a67ea0/ sign_companyid
# e9a10972-3759-432d-8dd9-82b04cf665eb/ survey_repost_id
# yzjcsdev?key=d8014cf2