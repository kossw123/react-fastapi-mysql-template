// import { create } from "zustand";

// // // create라는 함수 안에 () => ()라는 무명함수를 생성하고 { ... }를 반환
// // // 모든 형식이 똑같다. () => ()라는 무명함수 안에 { ... }라는 객체를 반환한다.

// // // const useBear = create((set) => ({ ... }))
// // //      1. create(...): Zustand에게 "지금부터 상태 창고 하나 만들어줘"라고 요청하는 명령입니다.
// // //      2. (set) => ({ ... }): 앞서 질문하신 () => ({}) 문법입니다! 창고를 만들면서 초기 데이터와 함수들이 담긴 객체({ ... })를 통째로 반환하는 것입니다.
// // //      3. (set): Zustand가 우리에게 넘겨주는 '창고 데이터 수정용 마법 지팡이(함수)'입니다. 데이터를 바꾸고 싶을 때는 무조건 이 set을 불러서 사용해야 합니다.
// // // 창고 내부에는 딱 두 종류의 데이터가 있다. 상태(Data)와 액션(함수)다.
// // // 여기서 명심할 것은 () => ({})와 같은 익명 함수를 만들어 바로 반환하는 문법을 많이 쓴다는 것이다.

// // // const useBear = create((set) => ({
// // //     bears: 0,
// // //     increaseMovement: () => set((state) => ({ bears: state.bears + 1 })),
// // //     decreaseMovement: () => set((state) => ({ bears: state.bears - 1 })),
// // //     removeAllBears: () => set({ bears: 0 }),
// // //     updateBears: (newBears) => set({ bears: newBears })
// // // }));

// // // 1. Zustand에서 데이터를 바꿀 때는 무조건 set(...)을 쓴다.
// // // 2. 기존 값이 계산에 필요하면 set((state) => ({ 변경할값 }))을 쓴다.
// // // 3. 기존 값과 상관없이 새로 덮어쓸 거면 set({ 변경할값 })을 쓴다.
// // // 4. increaseMovmenet: () => set(() => ({ ... }))에서 다음과 같은 set(() => ())은 클로저(Closure) 형태를 띈다.
// // //

// // const countStore = create((state) => ({
// //   count: 0,
// //   increase: () => state((component) => ({ count: component.count + 1 })),
// //   decrase: () => state((component) => ({ count: component.count - 1 })),
// // }));

// // function create(state) {
// //     return {
// //         count: 0,
// //         increase: () => state((component) => ({ count: component.count + 1 })),
// //         decrease: () => state((component) => ({ count: component.count - 1 })),
// //     }
// // }

// // // // 1. Zustand 라이브러리가 실제로 만들어 둔 create 함수의 내부 모습
// // // function create(익명함수공장) {
// // //   // Zustand가 내부적으로 관리하는 실제 데이터 저장소
// // //   let 내부_진짜_상태 = { count: 0 };

// // //   // 상태를 변경해주는 진짜 강력한 알맹이 함수 (우리가 set이라고 부르던 것)
// // //   function 상태_변경_함수(상태_업데이트_콜백) {
// // //     // 사용자가 준 콜백 함수에 '현재 상태'를 주입해서 새로운 값을 계산함
// // //     const 변경된_일부_상태 = 상태_업데이트_콜백(내부_진짜_상태);

// // //     // 기존 상태와 새로운 상태를 합침 (Shallow Merge)
// // //     내부_진짜_상태 = { ...내부_진짜_상태, ...변경된_일부_상태 };

// // //     // (참고: 상태가 바뀌었으니 리액트 컴포넌트들에게 화면을 다시 그리라고 신호를 보냄)
// // //   }

// // //   // 사용자가 전달해 준 익명함수공장에 '상태_변경_함수'를 주입해서 실행하고,
// // //   // 그 결과물(변수와 함수가 담긴 객체)을 반환함
// // //   return 익명함수공장(상태_변경_함수);
// // // }

// // // // 2. 우리가 실제로 선언해서 사용하는 코드
// // // const countStore = create((state) => {
// // //   return {
// // //     count: 0,
// // //     increase: function() {
// // //       // increase가 호출되면 주입받았던 state(상태_변경_함수)를 실행함!
// // //       state(function(component) {
// // //         return { count: component.count + 1 };
// // //       });
// // //     }
// // //   };
// // // });

// // counterStore.jsx
// const useCountStore = create((set) => ({
//   count: 0,
//   increase: () => set((state) => ({ count: state.count + 1 })),
//   decrease: () => set((state) => ({ count: state.count - 1 })),
// }));

// // CounterPage.jsx
// function Counter() {
//     // 이러면 useCounterStore가 반환하는 객체의 요소를 모두 가져올 수 있다.
//     const { count, increase, decrease } = useCounterStore();
//     // 그리고 count는 변수로, increase와 decrease는 함수로써 사용할 수 있다.
// }


// // create는 무조건 3개의 인자만 넘길 수 있다.
// // param1: 상태를 변경하는 함수를 의미한다. 보통 set이라고 칭한다.
// // param2: 현재 상태를 가져오는 함수를 의미한다. 보통 get이라 칭한다.
// // param3: 스토어 자체의 핵심 기능이 담긴 함수를 의미한다. 보통 store라 칭한다.
// // 만약 이에 따른 순서를 변경하면 런타임 오류가 발생하기에 무조건 3개의 인자의 순서는 고정되어 있다.
// const useCounterStore = create((param1, param2, param3) => ({ ... }));
// const useCounterStore = create((set, get, store) => ({ ... }));




// // persist 적용하는 방법
// const useCounterStore = create(() => ({ ... }))
// //persist를 적용하면 create의 내부 요소를 감싼 형태로 바꾸면 된다. 
// const useCounterStore = create(persist(() => ({ ... })))


// // persist를 사용하려면 persist인 두 번째 인자로 브라우저 storage에 저장될 key의 이름을 적어야 한다.
// const useCounterStore = create(persist(() => ({}), {}))
// // persist(param1, param2)에서 param2를 의미하는 객체에서는 name이라는 속성을 필수로 사용해야 한다.
// const useCounterStore = create(persist(() => ({}), { name: 'counter-storage' }))