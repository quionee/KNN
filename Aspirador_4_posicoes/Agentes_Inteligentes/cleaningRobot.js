// In this simple problem the world includes both the environment and the robot
// but in most problems the environment and world would be separate
class World {
    constructor(numFloors) {
        this.location = 0;
        this.floors = [];
        for (let i = 0; i < numFloors; i++) {
            this.floors.push({dirty: false});
        }
    }

    markFloorDirty(floorNumber) {
        this.floors[floorNumber].dirty = true;
    }

    simulate(action) {
        switch(action) {
        case 'SUCK':
            this.floors[this.location].dirty = false;
            break;
        case 'LEFTUP':
            this.location = 0;
            break;
        case 'RIGHTUP':
            this.location = 1;
            break;
        case 'LEFTDOWN':
            this.location = 2;
            break;
        case 'RIGHTDOWN':
            this.location = 3;
            break;
        }

        return action;
    }
}


// Rules are defined in code
function reflexVacuumAgent(world) {
    if (world.floors[world.location].dirty) {
        return 'SUCK';
    }
    else if (world.location == 0) {
        return 'RIGHTUP';
    }
    else if (world.location == 1) {
        return 'RIGHTDOWN';
    }
    else if (world.location == 2) {
        return 'LEFTUP';
    }
    else if (world.location == 3) {
        return 'LEFTDOWN';
    }
}

// Rules are defined in data, in a table indexed by [location][dirty]
function tableVacuumAgent(world, table) {
    let location = world.location;
    let dirty = world.floors[location].dirty ? 1 : 0;
    return table[location][dirty];
}

// world = new World(4);

// console.log(world);

// world.floors[1].dirty = 

// let dirty = world.floors[0].dirty ? 1 : 0;

// console.log(dirty);