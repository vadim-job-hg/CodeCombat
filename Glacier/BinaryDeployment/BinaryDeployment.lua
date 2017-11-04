local fs = self:findFriends()
for i = 1, #fs do
  local b = fs[i].deployment
  if fs[i].type == "paladin" then
    for j = 1, 8 do
      if b % 2 == 0 then
        self:summon("soldier")
      else
        self:summon("archer")
      end
      local ns = self:findFriends()
      self:command(ns[#ns], "move", {x=66-6*j, y=fs[i].pos.y})
      b = math.floor(b/2)
    end
  else
    for j = 1, 8 do
      if b % 3 == 0 then
        self:summon("soldier")
      elseif b % 3 == 1 then
        self:summon("archer")
      else
        self:summon("griffin-rider")
      end
      local ns = self:findFriends()
      self:command(ns[#ns], "move", {x=66-6*j, y=fs[i].pos.y})
      b = math.floor(b/3)
    end
  end
end
