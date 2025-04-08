import { useState, useEffect } from 'react';
import axios from 'axios';

type Item = {
  name: string;
  card_type: string;
  heal?: number;
  atk?: number;
  equiped?: boolean;
}

function BattleField() {
  const [hp, setHp] = useState(20);
  const [power, setPower] = useState(1);
  const [enemy, setEnemy] = useState()
  const [items, setItems] = useState<Item[]>([])
  const [gameOver, setGameOver] = useState(false)
  const api = axios.create({
    baseURL: 'http://localhost:8000/api/v1/cards'
  });
  
  useEffect(() => {
    if(!enemy){
        getEnemy()
    }
    if(enemy?.hp < 1){
        getVictory()
        getEnemy()
    }
  }, [enemy]);

  useEffect(() => {
    if(hp < 1){
        setGameOver(true)
    }
  }, [hp])

  const getEnemy = async () => {
    try {
      const res = await api.get('/enemy');
      setEnemy(res.data)
    } catch (error) {
      console.error('Error fetching enemy:', error);
    }
  };
  const getVictory = async () => {
    try {
      const res = await api.get('/victory');
      // window.alert('You found a '+res.data.name)
      setItems([...items, res.data])
    } catch (error) {
      console.error('Error fetching prize:', error);
    }
  };

  const useItem = (item: Item) => {
    const currentPounch = items
    if(item.heal){
      setHp(hp+item.heal)
    }
    if(item.atk){
      const equipedItem = currentPounch.find(i=>i.equiped)
      let pow = power
      if(equipedItem){
        equipedItem.equiped = false
        pow -= equipedItem?.atk || 0
      }
      item.equiped = true
      setPower(pow+item.atk)
    }
    if(item.card_type == 'consumable'){
      const index = currentPounch.findIndex((i => i.name === item.name))
      currentPounch.splice(index, 1)
    }
    setItems(currentPounch)
  }

  const handleAttack = () => {
    // TODO set inititative
    setHp(hp-(enemy?.atk || 0))
    setEnemy({...enemy, hp: enemy.hp-power})
  }

  if(gameOver){
    return <div>Game Over</div>
  }

  return (
    <>
        <h1 className='absolute text-red-500 top-5 right-[45%]'>HP: {hp}</h1>
        <h1 className='absolute text-orange-500 top-5 right-[55%]'>ATK: {power}</h1>
        <div className='cursor-pointer w-auto' onClick={() => handleAttack()}>
            <span className='absolute right-[50%]'>{enemy?.name}</span>
        </div>
        <div className='absolute top-10 right-10'>
          <h3>Pouch</h3>
          {items.map((i, index)=>(<span className={`cursor-pointer ${i.equiped && 'text-green-400'} block select-none`} title={`+${i.atk || i.heal}`} key={index} onClick={() => useItem(i)}>{i.name}</span>))}
        </div>
    </>
  );
}

export default BattleField;