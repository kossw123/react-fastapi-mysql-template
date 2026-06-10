import { create } from 'zustand';


//
// const useBear = create((set) => ({ ... }))
//      1. create(...): Zustand에게 "지금부터 상태 창고 하나 만들어줘"라고 요청하는 명령입니다.
//      2. (set) => ({ ... }): 앞서 질문하신 () => ({}) 문법입니다! 창고를 만들면서 초기 데이터와 함수들이 담긴 객체({ ... })를 통째로 반환하는 것입니다.
//      3. (set): Zustand가 우리에게 넘겨주는 '창고 데이터 수정용 마법 지팡이(함수)'입니다. 데이터를 바꾸고 싶을 때는 무조건 이 set을 불러서 사용해야 합니다.
// 창고 내부에는 딱 두 종류의 데이터가 있다. 상태(Data)와 액션(함수)다.
// 여기서 명심할 것은 () => ({})와 같은 익명 함수를 만들어 바로 반환하는 문법을 많이 쓴다는 것이다.

// const useBear = create((set) => ({
//     bears: 0,
//     increaseMovement: () => set((state) => ({ bears: state.bears + 1 })),
//     decreaseMovement: () => set((state) => ({ bears: state.bears - 1 })),
//     removeAllBears: () => set({ bears: 0 }),
//     updateBears: (newBears) => set({ bears: newBears })
// }));


// 1. Zustand에서 데이터를 바꿀 때는 무조건 set(...)을 쓴다.
// 2. 기존 값이 계산에 필요하면 set((state) => ({ 변경할값 }))을 쓴다.
// 3. 기존 값과 상관없이 새로 덮어쓸 거면 set({ 변경할값 })을 쓴다.

// 이 개념을 잡고 나면, 앞으로 어떤 Zustand 코드를 보더라도 "아, 이건 데이터를 바꾸는 리모컨이구나!" 하고 쉽게 읽으실 수 있을 것입니다.

