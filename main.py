import streamlit as st

# MBTI 유형에 대한 설명 사전
mbti_descriptions = {
    'ISTJ': (
        '🔍 **ISTJ (검사관)**\n'
        '신중하고 실용적이며 체계적인 성향을 가진 ISTJ는 책임감과 신뢰성을 매우 중요시합니다.\n'
        '이들은 과거의 경험과 실제 데이터를 바탕으로 결정을 내리며,\n'
        '전통과 규칙을 존중하는 경향이 있습니다. 팀워크에서도 안정적인 역할을 하며,\n'
        '일관된 결과를 도출하는 것에 큰 자부심을 가지고 있습니다. '
        'ISTJ는 문제 해결에 강하며, 주변에게 믿음직한 조언자로 여겨집니다. '
        '일과 생활 모두에서 실질적이고 성실한 태도를 유지합니다. '
    ),
    'ISFJ': (
        '💖 **ISFJ (보호자)**\n'
        '사려 깊고 헌신적인 ISFJ는 주위 사람들을 돌보고 지원하는 것을 좋아합니다.\n'
        '그들은 남의 감정을 잘 이해하고, 필요한 경우 도움을 제공하는 데에 큰 만족을 느낍니다.\n'
        'ISFJ는 전통을 중시하며, 자신의 가치관에 따라 행동합니다. \n'
        '이들은 꼼꼼하고 세심하여, 작은 일에도 큰 관심을 기울입니다. '
        '가족이나 친구와의 소중한 관계를 위해 힘쓰며, 그들에게 안정감을 제공합니다. '
    ),
    'INFJ': (
        '🌈 **INFJ (옹호자)**\n'
        '창의적이고 통찰력 있는 INFJ는 깊은 감정을 가지고 있으며,\n'
        '자신만의 비전과 목표에 따라 행동합니다. 이들은 다른 사람들을 이해하고,\n'
        '그들의 잠재력을 끌어내기 위해 강한 인내심을 가집니다. \n'
        'INFJ는 어떤 대의명分을 위해 싸우며, 세상을 더 나은 곳으로 만들기 위한 열정을 가지고 있습니다. '
        '그들의 직관력은 사람들과의 깊은 교감을 가능하게 하며,\n'
        '종종 다른 사람들에게 영감을 주는 역할을 합니다. '
    ),
    'INTJ': (
        '🧠 **INTJ (전략가)**\n'
        '분석적이고 독립적인 INTJ는 깊이 있는 사고와 계획을 중요시합니다.\n'
        '이들은 혁신적인 아이디어를 개발하고, 목표를 설정하여 달성하는 것에 집중합니다. \n'
        '자신의 지식을 통해 문제를 해결하고, 미래를 설계하는 능력이 뛰어납니다. '
        'INTJ는 다른 사람들의 의견에 휘둘리지 않으며, 자신의 길을 가기 위해 노력합니다. '
    ),
    'ISTP': (
        '⚙️ **ISTP (장인)**\n'
        '실용적이고 사실적인 ISTP는 문제 해결에 강하며,\n'
        '즉흥적으로 행동하는 경향이 있습니다. 이들은 주변 환경을 관찰하고,\n'
        '직접적인 경험을 통해 배우는 것을 좋아합니다. \n'
        'ISTP는 뛰어난 손재주를 가지고 있으며,\n'
        '소프트웨어나 다양한 기술적 문제를 해결하는 데에 탁월한 능력을 보입니다. '
    ),
    'ISFP': (
        '🎨 **ISFP (예술가)**\n'
        '사람들에게 다정하고 감성적인 ISFP는 예술과 창의력에 높은 가치를 둡니다.\n'
        '이들은 자연과 아름다움에 민감하며, 자신만의 독특한 방식으로 세상을 표현합니다. \n'
        'ISFP는 순간의 기쁨을 추구하며,\n'
        '변화를 수용하고 자신의 감정을 솔직하게 드러냅니다. '
    ),
    'INFP': (
        '🌟 **INFP (중재자)**\n'
        '이상적이고 사색적인 INFP는 깊은 감정과 강한 가치관을 가지고 있습니다.\n'
        '이들은 자신과 주변 사람들을 이해하기 위해 노력하며, 감정적인 지지를 제공합니다. \n'
        'INFP는 다양성과 자아 탐구를 사랑하며,\n'
        '대의에 대한 열정이 강하여 세상에 긍정적인 영향을 미치고자 합니다. '
    ),
    'INTP': (
        '🧩 **INTP (논리가)**\n'
        '호기심이 많고 분석적인 INTP는 복잡한 문제를 해결하고,\n'
        '새로운 아이디어를 탐구하는 것을 두려워하지 않습니다. \n'
        '이들은 깊이 있는 통찰력을 가지고 있으며, 세상을 이해하기 위해 끊임없이 질문합니다. '
        'INTP는 이론과 시스템, 논리에 대한 관심이 많으며,\n'
        '창의성을 발휘하여 혁신적인 해결책을 제시합니다. '
    ),
    'ESTP': (
        '🚀 **ESTP (활동가)**\n'
        '활동적이고 실용적인 ESTP는 즉각적인 결과를 중시하며,\n'
        '현실적이고 사실적인 접근 방식을 취합니다. \n'
        '이들은 새로운 경험을 찾고 모험을 즐기는 데 큰 흥미를 보이며,\n'
        '다른 사람들과의 사회적 상호작용에서 큰 에너지를 얻습니다. '
    ),
    'ESFP': (
        '🎉 **ESFP (연예인)**\n'
        '사교적이고 에너지가 넘치는 ESFP는 현재 순간을 즐기는 것을 최우선으로 하고,\n'
        '다양한 활동을 통해 남들과의 관계를 소중히 여깁니다. \n'
        '이들은 상황에 즉각적으로 반응하며, 주변 환경에서 즐거움을 찾습니다. '
        'ESFP는 긍정적인 에너지를 주변과 나누며, 다른 사람들을 즐겁게 하는 것을 좋아합니다. '
    ),
    'ENFP': (
        '🎇 **ENFP (재기발랄한 설명자)**\n'
        '창의적이고 자유로운 영혼인 ENFP는 새로운 가능성을 탐구하며,\n'
        '사람들과의 깊은 교감을 중요시합니다. \n'
        '이들은 정열적이고 열정적이며,\n'
        '다양한 아이디어를 제안하고 실천하는 데 큰 흥미를 보입니다. '
    ),
    'ENTP': (
        '💡 **ENTP (발명가)**\n'
        '호기심이 많고 창의적인 ENTP는 끊임없이 새로운 아이디어를 발굴하며,\n'
        '문제를 다양한 관점에서 바라보는 능력이 뛰어납니다. \n'
        '이들은 지적 대화를 즐기고, 새로운 이론을 탐구하는 데 매력을 느낍니다. '
    ),
    'ESTJ': (
        '🛠️ **ESTJ (관리자)**\n'
        '조직적이고 목표 지향적인 ESTJ는 체계적인 접근 방식을 취하며,\n'
        '효율성을 중시합니다. 이들은 정해진 규칙과 절차를 따르며,\n'
        '강력한 리더십을 발휘하여 팀을 이끌어가는 데 능숙합니다. '
    ),
    'ESFJ': (
        '🌺 **ESFJ (사교가)**\n'
        '사교적이고 협력적인 ESFJ는 주변 사람들에게 큰 관심을 갖고,\n'
        '그들이 필요로 할 때 항상 도움이 되고자 합니다. \n'
        '이들은 팀워크를 중시하고, 조화를 이루는 데 기여합니다. '
    ),
    'ENFJ': (
        '🌟 **ENFJ (주도자)**\n'
        '따뜻하고 카리스마 있는 ENFJ는 사람들을 이끄는 능력이 뛰어나며,\n'
        '자연스럽게 다른 사람들에게 영감을 줍니다. \n'
        '이들은 주변의 감정에 민감하며, 항상 긍정적인 변화를 추구합니다. '
    ),
    'ENTJ': (
        '🔥 **ENTJ (지도자)**\n'
        '결단력 있고 전략적인 ENTJ는 목표 지향적이며,\n'
        '리더십과 관리 능력이 뛰어납니다. 이들은 조직의 성공을 위해 계획하고 개발하는 데 능숙합니다. \n'
        'ENTJ는 매우 의욕적이며,\n'
        '어떤 장애물도 극복하려고 하는 포부를 가지고 있습니다. '
    ),
}

def main():
    st.title("MBTI 선택기 🌈")

    # MBTI 유형 선택
    mbti_type = st.selectbox("당신의 MBTI 유형을 선택하세요:", list(mbti_descriptions.keys()))

    # 선택된 MBTI 유형에 대한 설명 출력
    st.write("당신의 MBTI 유형은: **", mbti_type, "**")
    st.write("설명:\n", mbti_descriptions[mbti_type])

# 앱 실행
if __name__ == "__main__":
    main()
