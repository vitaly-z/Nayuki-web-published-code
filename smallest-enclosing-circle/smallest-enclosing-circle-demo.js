/*
 * Smallest enclosing circle - Demo (compiled from TypeScript)
 *
 * Copyright (c) 2022 Project Nayuki
 * https://www.nayuki.io/page/smallest-enclosing-circle
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this program (see COPYING.txt and COPYING.LESSER.txt).
 * If not, see <http://www.gnu.org/licenses/>.
 */
"use strict";
// DOM elements
let svgElem = document.querySelector("article svg");
let staticRadio = document.getElementById("random-static");
let movingRadio = document.getElementById("random-moving");
let manualRadio = document.getElementById("manual-position");
// Constants and mutable state
const POINT_RADIUS = 0.012;
let points = [];
let draggingPointIndex = -1;
function initialize() {
    handleRadioButtons();
    svgElem.onmousedown = ev => handleMouse(ev, "down");
    svgElem.onmousemove = ev => handleMouse(ev, "move");
    svgElem.onmouseup = ev => handleMouse(ev, "up");
    svgElem.onselectstart = ev => ev.preventDefault();
    function handleMouse(ev, type) {
        // Calculate SVG coordinates
        const bounds = svgElem.getBoundingClientRect();
        const width = bounds.width / Math.min(bounds.width, bounds.height);
        const height = bounds.height / Math.min(bounds.width, bounds.height);
        const evX = ((ev.clientX - bounds.left) / bounds.width - 0.5) * width;
        const evY = ((ev.clientY - bounds.top) / bounds.height - 0.5) * height;
        if (type == "down") {
            // Find nearest existing point
            let nearestIndex = -1;
            let nearestDist = Infinity;
            points.forEach((point, index) => {
                const dist = Math.hypot(point.x - evX, point.y - evY);
                if (dist < nearestDist) {
                    nearestDist = dist;
                    nearestIndex = index;
                }
            });
            if (ev.button == 0) {
                if (nearestIndex != -1 && nearestDist < POINT_RADIUS * 1.5)
                    draggingPointIndex = nearestIndex;
                else {
                    draggingPointIndex = points.length;
                    points.push(new MovingPoint(NaN, NaN, NaN, NaN));
                }
                points[draggingPointIndex] = new MovingPoint(evX, evY, 0, 0);
            }
            else if (ev.button == 2) {
                if (nearestIndex != -1 && nearestDist < POINT_RADIUS * 1.5)
                    points.splice(nearestIndex, 1);
                if (nearestDist < POINT_RADIUS * 5) {
                    svgElem.oncontextmenu = ev => {
                        ev.preventDefault();
                        svgElem.oncontextmenu = null;
                    };
                }
            }
            else
                return;
            manualRadio.checked = true;
            handleRadioButtons();
        }
        else if (type == "move" || type == "up") {
            if (draggingPointIndex == -1)
                return;
            points[draggingPointIndex] = new MovingPoint(evX, evY, 0, 0);
            if (type == "up")
                draggingPointIndex = -1;
        }
        else
            throw new Error("Assertion error");
        showPointsAndCircle();
    }
}
window.addEventListener("DOMContentLoaded", initialize);
function handleRadioButtons() {
    staticDemo.stop();
    movingDemo.stop();
    if (staticRadio.checked)
        staticDemo.start();
    if (movingRadio.checked)
        movingDemo.start();
}
var staticDemo;
(function (staticDemo) {
    let timeout = null;
    function start() {
        const NUM_POINTS = Math.round(Math.pow(40, Math.random()) * 2);
        points = [];
        for (let i = 0; i < NUM_POINTS; i++)
            points.push(new MovingPoint(randomGaussian() * 0.14, randomGaussian() * 0.14, 0, 0));
        showPointsAndCircle();
        timeout = window.setTimeout(start, 3000);
    }
    staticDemo.start = start;
    function stop() {
        if (timeout !== null) {
            clearTimeout(timeout);
            timeout = null;
        }
    }
    staticDemo.stop = stop;
})(staticDemo || (staticDemo = {}));
var movingDemo;
(function (movingDemo) {
    let timeout = null;
    function start() {
        const NUM_POINTS = 15;
        points = [];
        for (let i = 0; i < NUM_POINTS; i++)
            points.push(new MovingPoint(randomGaussian() * 0.10, randomGaussian() * 0.10, randomGaussian() * 0.04, randomGaussian() * 0.04));
        const time = performance.now();
        update(time, time);
    }
    movingDemo.start = start;
    function update(prevTime, curTime) {
        showPointsAndCircle();
        const deltaTime = Math.min(curTime - prevTime, 1000) / 1000;
        const bounds = svgElem.getBoundingClientRect();
        const width = bounds.width / Math.min(bounds.width, bounds.height);
        const height = bounds.height / Math.min(bounds.width, bounds.height);
        for (let i = 0; i < points.length; i++) {
            let p = points[i];
            p.x += p.vx * deltaTime;
            p.y += p.vy * deltaTime;
            if (Math.hypot(p.x, p.y) > 0.5)
                points[i] = new MovingPoint(randomGaussian() * 0.10, randomGaussian() * 0.10, randomGaussian() * 0.04, randomGaussian() * 0.04);
        }
        timeout = requestAnimationFrame(nextTime => update(curTime, nextTime));
    }
    function stop() {
        if (timeout !== null) {
            cancelAnimationFrame(timeout);
            timeout = null;
        }
    }
    movingDemo.stop = stop;
})(movingDemo || (movingDemo = {}));
function showPointsAndCircle() {
    let offCircleGroupElem = svgElem.querySelectorAll("g")[0];
    let onCircleGroupElem = svgElem.querySelectorAll("g")[1];
    while (offCircleGroupElem.firstChild !== null)
        offCircleGroupElem.removeChild(offCircleGroupElem.firstChild);
    while (onCircleGroupElem.firstChild !== null)
        onCircleGroupElem.removeChild(onCircleGroupElem.firstChild);
    let circle = makeCircle(points);
    let circleElem = svgElem.querySelector("circle");
    if (circle === null) {
        circleElem.setAttribute("r", "0");
        return;
    }
    circleElem.setAttribute("cx", circle.x.toString());
    circleElem.setAttribute("cy", circle.y.toString());
    circleElem.setAttribute("r", circle.r.toString());
    for (const point of points) {
        let circElem = document.createElementNS(svgElem.namespaceURI, "circle");
        circElem.setAttribute("cx", point.x.toString());
        circElem.setAttribute("cy", point.y.toString());
        circElem.setAttribute("r", POINT_RADIUS.toString());
        const dist = Math.hypot(point.x - circle.x, point.y - circle.y) / circle.r;
        if (circle.r == 0 || 1 / MULTIPLICATIVE_EPSILON < dist && dist < MULTIPLICATIVE_EPSILON)
            onCircleGroupElem.appendChild(circElem);
        else
            offCircleGroupElem.appendChild(circElem);
    }
}
function randomGaussian() {
    return Math.sqrt(-2 * Math.log(Math.random())) * Math.cos(Math.random() * Math.PI * 2);
}
class MovingPoint {
    constructor(x, y, vx, vy) {
        this.x = x;
        this.y = y;
        this.vx = vx;
        this.vy = vy;
    }
}
