import { useState, useEffect } from 'react';
import axios from 'axios';

function BattleField() {
  const [hp, setHp] = useState(20);
  const [power, setPower] = useState(1);
  const [enemy, setEnemy] = useState()
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
      window.alert('You found a '+res.data.name)
      if(res.data.heal){
        setHp(hp+res.data.heal)
      }
      if(res.data.atk){
        setPower(res.data.atk)
      }
    } catch (error) {
      console.error('Error fetching prize:', error);
    }
  };

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
        <h1 className='absolute text-red-500 top-5 right-[50%]'>{hp}</h1>
        <div className='cursor-pointer w-auto' onClick={() => handleAttack()}>
            <span className='absolute right-[50%]'>{enemy?.name}</span>
        </div>
    </>
  );
}

export default BattleField;