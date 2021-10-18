const fileSyncOrder = (files, storageLimit, uploadSpeed, duration) => {
    // make sure files is order by time line
    files = files.map((file, index) => [...file, index])
    files = files.sort((file, file1) => file[1] - file1[1])

    console.log('input: ', JSON.stringify({
        files,
        storageLimit,
        uploadSpeed,
        duration
    }))

    const uploadTime = size => size / uploadSpeed
    const uploadTimes = files.map(file => uploadTime(file[0]))
    // Dropbox uploads files one-by-one and prioritizes them based on size,
    // starting with the smallest.
    const getMinArr = arr => {
        let min = [arr[0], 0]
        for (let ind = 1; ind < arr.length; ind++) {
            min[0][0] > arr[ind][0] && (min = [arr[ind], ind])
        }
        return min
    }
    //
    let res = []
    let durationTime = files[0][1]
    let limitFileSize = 0
    let queues = []
    let index = 0
    for (; durationTime <= duration;) {

        let pos = index + 1
        if (index < files.length) {
            durationTime >= files[index][1] && queues.push(files[index])
            while (pos < files.length && files[index][1] === files[pos][1]) {
                queues.push(files[pos])
                pos++
            }
        }

        console.log('index', index, 'queues', JSON.stringify(queues), 'durationTime', durationTime)

        if (index > 0 && queues.length === 0) {
            break;
        }
        const minArray = getMinArr(queues)
        const minFile = minArray[0]
        // remove on queue
        queues.splice(minArray[1], 1);
        const upTime = uploadTimes[minFile[2]]
        if (limitFileSize + minFile[0] <= storageLimit &&
            durationTime + upTime <= duration) {
            limitFileSize += minFile[0]
            res.push(minFile[2])
        }

        let posNext = pos;
        while (posNext < files.length &&
            files[posNext][1] < durationTime + upTime) {
            queues.push(files[posNext])
            posNext++
        }
        console.log('durationTime + upTime', durationTime + upTime)
        durationTime = posNext < files.length ? files[posNext][1] : durationTime + upTime
        console.log('durationTime1', durationTime)
        index = posNext
    }
    return res
}
