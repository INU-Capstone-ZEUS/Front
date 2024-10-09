import {react, useState} from 'react'

export default function ConditionalSearcher() {

    const [expression, setExpression] = useState(); // 조건식
    const [list, setList] = useState([]); // 할일 목록
    const btnAddList = () => {
        // 기록하기 클릭
        if (!expression) return;
        setList([...list, expression]);
        setExpression("");
    };



    return (
        <section id='conditional-searcher'>

        </section>
    )
}